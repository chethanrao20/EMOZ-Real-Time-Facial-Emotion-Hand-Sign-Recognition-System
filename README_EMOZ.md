# EMOZ — updated frontend

This update adds a responsive HTML/CSS/JavaScript frontend while keeping the original `app.py`, training scripts, utility files, and backups unchanged.

## Run the new web frontend (Windows CMD)

1. Extract the ZIP.
2. Open Command Prompt in the extracted `EMOZ_Updated` folder.
3. Activate your existing virtual environment if you have one.
4. Install the added dependencies (this may take a while because DeepFace/TensorFlow are large):

   ```bat
   python -m pip install -r requirements.txt
   ```

5. Start the EMOZ web app:

   ```bat
   python web_app.py
   ```

6. Open `http://127.0.0.1:5000` in your browser.
7. Allow camera permission. Start Camera, then click Analyze Frame. You can also upload a JPG/PNG/WEBP image.

The frontend calls `POST /api/analyze`; image analysis is handled by DeepFace on the local Python server. The first analysis may download model weights and can take longer.

## Original application

Your original `app.py` is preserved. To run its Streamlit interface instead, use:

```bat
python -m streamlit run app.py
```

Run one server at a time if you want to avoid confusion.

## Important note about model files

The uploaded files did not include binary model artifacts such as `face_emotion_model.h5` or `voice_emotion_svm.joblib`, nor the datasets. Those were not created or replaced by this frontend update. The new API uses DeepFace's emotion analysis engine and may download its own model weights on first run.

## Notes

- Camera access normally requires `localhost` or HTTPS.
- Predictions estimate visible facial expression and are not reliable measurements of a person's internal feelings.
- Original `app.py` and the original model-training scripts are retained as uploaded.
