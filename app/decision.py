# app/decision.py
def plan_grasp(detections):
    for obj in detections:
        if obj["confidence"] > 0.6:
            return {
                "action": "GRASP",
                "object": obj["class"],
                "position": obj["bbox"]
            }

    return {"action": "NO_ACTION"}
