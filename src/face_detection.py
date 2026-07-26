import cv2
import os


class FaceDetector:

    def __init__(self):

        base_dir = os.path.dirname(os.path.abspath(__file__))

        model_path = os.path.join(
            base_dir,
            "..",
            "models",
            "haarcascade_frontalface_default.xml"
        )

        self.face_cascade = cv2.CascadeClassifier(model_path)

        if self.face_cascade.empty():
            raise FileNotFoundError(
                f"Cannot load Haar Cascade : {model_path}"
            )

    def detect(self, frame):

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(80, 80)
        )

        return faces

    def draw(self, frame, faces):

        for (x, y, w, h) in faces:

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

        return frame
