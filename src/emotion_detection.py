import time
from deepface import DeepFace


class EmotionDetector:

    def __init__(self):

        self.last_emotion = "neutral"
        self.last_detect_time = 0
        self.detect_interval = 1.0  # Detect every 1 second

    def detect(self, face):

        now = time.time()

        # Return previous emotion if interval not completed
        if now - self.last_detect_time < self.detect_interval:
            return self.last_emotion

        self.last_detect_time = now

        try:

            result = DeepFace.analyze(
                face,
                actions=["emotion"],
                detector_backend="opencv",
                enforce_detection=False,
                silent=True
            )

            if isinstance(result, list):
                result = result[0]

            self.last_emotion = result["dominant_emotion"]

        except Exception as e:

            print("Emotion Error :", e)

        return self.last_emotion
