from picamera2 import Picamera2
import cv2

class Camera:

    def __init__(self):
        self.picam2 = Picamera2()

        config = self.picam2.create_preview_configuration(
            main={"size": (640, 480)}
        )

        self.picam2.configure(config)
        self.picam2.start()

    def get_frame(self):
        frame = self.picam2.capture_array()

        # RGB → BGR
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        return frame

    def stop(self):
        self.picam2.stop()
