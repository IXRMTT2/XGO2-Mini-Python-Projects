import cv2
from xgoedu import XGOEDU
from xgolib import XGO
import time

XGO_edu = XGOEDU()
dog = XGO('xgomini')

def emotion_recognition():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # Set width
    cap.set(4, 480)  # Set height

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            emotion = XGO_edu.emotion()
            print(f"Detected emotion: {emotion}")

            if emotion == "happy":
                dog.action(1)  # Perform a happy action
                print("Performing happy action...")
            elif emotion == "sad":
                dog.action(2)  # Perform a sad action
                print("Performing sad action...")
            elif emotion == "angry":
                dog.action(3)  # Perform an angry action
                print("Performing angry action...")
            else:
                dog.action(0)  # Default action
                print("Performing default action...")

            cv2.imshow('Emotion Recognition', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        print("Interrupted by user")

    finally:
        cap.release()
        cv2.destroyAllWindows()
        dog.perform(0)  # Ensure the robot stops
        print("Stopped the robot")

if __name__ == "__main__":
    emotion_recognition()