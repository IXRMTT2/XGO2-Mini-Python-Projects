import cv2
from xgoedu import XGOEDU
from xgolib import XGO
import time

XGO_edu = XGOEDU()
dog = XGO('xgomini')

def qr_code_recognition():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # Set width
    cap.set(4, 480)  # Set height

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            qr_code = XGO_edu.QRRecognition()
            print(f"Detected QR code: {qr_code}")

            if qr_code == "forward":
                dog.move_x(15)  # Move forward
                print("Moving forward...")
            elif qr_code == "stop":
                dog.perform(0)  # Stop the robot
                print("Stopping...")
            elif qr_code == "turn_left":
                dog.turn(-100)  # Turn left
                print("Turning left...")
            elif qr_code == "turn_right":
                dog.turn(100)  # Turn right
                print("Turning right...")
            else:
                dog.perform(0)  # Default action
                print("No valid QR code detected, stopping...")

            cv2.imshow('QR Code Recognition', frame)

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
    qr_code_recognition()