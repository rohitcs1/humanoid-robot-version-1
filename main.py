import cv2
from camera import Camera
from face_detection import FaceDetector

camera = Camera()
detector = FaceDetector()

print("Press Q to Exit")

while True:

    frame = camera.get_frame()

    faces = detector.detect(frame)

    frame = detector.draw(frame, faces)

    cv2.putText(
        frame,
        f"Faces : {len(faces)}",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    cv2.imshow("Robot Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.stop()

cv2.destroyAllWindows()
