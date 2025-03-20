import cv2
from xgoedu import XGOEDU
from xgolib import XGO
import time

XGO_edu = XGOEDU()
dog = XGO('xgomini')

def gesture_recognition():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # Set width
    cap.set(4, 480)  # Set height

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            gesture = XGO_edu.gestureRecognition()
            print(f"Detected gesture: {gesture}")

            if gesture == "wave":
                dog.action(1)  # Perform a wave action
                print("Performing wave action...")
            elif gesture == "thumbs_up":
                dog.action(2)  # Perform a thumbs up action
                print("Performing thumbs up action...")
            elif gesture == "thumbs_down":
                dog.action(3)  # Perform a thumbs down action
                print("Performing thumbs down action...")
            else:
                dog.action(0)  # Default action
                print("Performing default action...")

            cv2.imshow('Gesture Recognition', frame)

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
    gesture_recognition()