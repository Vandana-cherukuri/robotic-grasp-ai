# app/main.py
from fastapi import FastAPI
import cv2
from detector import detect_objects
from decision import plan_grasp

app = FastAPI()
camera = cv2.VideoCapture(0)

@app.get("/detect")
def detect():
    ret, frame = camera.read()
    detections = detect_objects(frame)
    decision = plan_grasp(detections)

    return {
        "detections": detections,
        "decision": decision
    }
