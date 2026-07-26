import cv2

from camera import Camera
from face_detection import FaceDetector
from emotion_detection import EmotionDetector
from display import RobotFace


def main():

    camera = Camera()
    detector = FaceDetector()
    emotion_detector = EmotionDetector()
    robot = RobotFace()

    # Startup Screen
    robot.show_name()

    current_emotion = None
    face_detected = False

    print("=" * 40)
    print("      ALPHA AI ROBOT")
    print("Press Q to Exit")
    print("=" * 40)

    while True:

        frame = camera.get_frame()

        if frame is None:
            continue

        faces = detector.detect(frame)

        # No face found
        if len(faces) == 0:

            if face_detected:
                face_detected = False
                current_emotion = None
                robot.show_name()

            cv2.putText(
                frame,
                "Searching Face...",
                (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 255),
                2
            )

        else:

            face_detected = True

            # Take first detected face
            (x, y, w, h) = faces[0]

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            face = frame[y:y+h, x:x+w]

            emotion = emotion_detector.detect(face)

            # Emotion above face
            cv2.putText(
                frame,
                emotion.upper(),
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

            # Emotion on top-left
            cv2.putText(
                frame,
                f"Emotion : {emotion.upper()}",
                (15, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 0),
                2
            )

            # Update OLED only when emotion changes
            if emotion != current_emotion:

                current_emotion = emotion

                print("Emotion :", emotion)

                if emotion == "happy":
                    robot.happy()

                elif emotion == "sad":
                    robot.sad()

                elif emotion == "angry":
                    robot.angry()

                else:
                    robot.neutral()

        cv2.imshow("ALPHA AI Robot", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    robot.clear()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
