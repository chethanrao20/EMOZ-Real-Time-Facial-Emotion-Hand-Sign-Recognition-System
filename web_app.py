"""EMOZ web frontend API. Original app.py is intentionally preserved."""
from flask import Flask, jsonify, request, send_from_directory
from deepface import DeepFace
import numpy as np
import cv2
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR / "frontend"
app = Flask(__name__, static_folder=str(FRONTEND_DIR), static_url_path="/assets")

@app.get("/")
def index():
    return send_from_directory(FRONTEND_DIR, "index.html")

@app.get("/<path:filename>")
def frontend_file(filename):
    # Only serve files from the frontend directory.
    return send_from_directory(FRONTEND_DIR, filename)

@app.post("/api/analyze")
def analyze():
    uploaded = request.files.get("image")
    if uploaded is None:
        return jsonify(error="Upload an image in the 'image' field."), 400
    raw = np.frombuffer(uploaded.read(), dtype=np.uint8)
    image = cv2.imdecode(raw, cv2.IMREAD_COLOR)
    if image is None:
        return jsonify(error="The uploaded file could not be read as an image."), 400
    try:
        results = DeepFace.analyze(
            img_path=image, actions=["emotion"], enforce_detection=True,
            detector_backend="opencv", silent=True
        )
        result = results[0] if isinstance(results, list) else results
        emotions = result.get("emotion", {})
        if not emotions:
            return jsonify(error="The model did not return emotion scores."), 502
        dominant = result.get("dominant_emotion") or max(emotions, key=emotions.get)
        region = result.get("region") or result.get("facial_area") or {}
        face_box = None
        if region and all(k in region for k in ("x", "y", "w", "h")):
            face_box = {k: int(region[k]) for k in ("x", "y", "w", "h")}
        return jsonify(emotion=dominant, confidence=round(float(emotions.get(dominant, 0)), 1),
                       scores={key: round(float(value), 1) for key, value in emotions.items()},
                       face=face_box, image_width=int(image.shape[1]), image_height=int(image.shape[0]))
    except Exception as exc:
        return jsonify(error=f"Analysis failed: {str(exc)[:240]}"), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
