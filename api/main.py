from fastapi import FastAPI, File, UploadFile
from fastapi import Body
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from feature_extraction import noise, stretch, shift, pitch, extract_features, get_features
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL = tf.keras.models.load_model("../models/models/1")

emotion_classes = ["sad", "disgust", "happy", "neutral", "angry", "calm", "surprise", "fear"]

@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI application!"}

@app.get("/ping")
async def ping():
    return "Hello, I am alive"

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    file_contents = await file.read()
    file_stream = BytesIO(file_contents)
    features = get_features(file_stream)
    # print(features)
    scaler = StandardScaler()
    features = scaler.fit_transform(features)
    # print("idjdjdjdjdjdj")
    # print(features)
    prediction = MODEL.predict(features)
    # Convert one-hot encoded prediction to class name
    confidence = np.max(prediction[0])
    predicted_emotion = emotion_classes[np.argmax(prediction[0])]

    return {"emotion": predicted_emotion,"confidence" :  float(confidence)}

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)