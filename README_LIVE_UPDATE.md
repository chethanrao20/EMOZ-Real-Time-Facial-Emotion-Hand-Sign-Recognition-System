# EMOZ live-analysis update

## What changed
- Camera mode now sends frames to the local DeepFace backend automatically after you start the camera; you no longer need to click Analyze for each frame.
- A green face-region box appears when the detector returns a face region.
- The right-hand analysis panel refreshes the top expression and all returned expression scores.
- Added a full-screen camera-stage toggle and kept the manual Analyze Now button.
- Frames are resized to a maximum width of 640px to reduce processing time. Updates are sequential so requests do not pile up; actual refresh rate depends on your computer and model speed.

## Run it
From Command Prompt:

```cmd
cd /d D:\EMOZ_Updated\EMOZ_Updated
.venv\Scripts\activate
python web_app.py
```

Open http://127.0.0.1:5000. Click **START LIVE ANALYSIS**, allow camera access, and keep the terminal open. Click **FULL SCREEN** to enlarge the camera view. Click **STOP** to end the camera session.

The model output is an estimate of visible facial-expression patterns, not a reliable measure of someone's internal emotional state. Use the camera with consent.


## Added feature: Real-time hand sign scanner

The frontend now includes a separate webcam-based hand scanner powered by MediaPipe Hands in the browser. It recognizes six basic gestures: Open Palm, Fist, Peace Sign, Thumbs Up, Thumbs Down, and Pointing. It runs independently of facial-expression analysis and does not upload its camera frames to the Flask server. Internet access is required to load MediaPipe from its CDN. This is a basic gesture demo, not full sign-language translation.
