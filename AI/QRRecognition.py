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

            qr_code = XGO_edu.QRRecognition(frame)
            print(f"Detected QR code: {qr_code}")

            if qr_code == "forward":
                dog.walk(direction=0, speed=50)  # Walk forward
                print("Walking forward...")
            elif qr_code == "stop":
                dog.stop()  # Stop the robot
                print("Stopping...")
            elif qr_code == "turn_left":
                dog.turn(direction=-1, speed=50)  # Turn left
                print("Turning left...")
            elif qr_code == "turn_right":
                dog.turn(direction=1, speed=50)  # Turn right
                print("Turning right...")
            else:
                dog.stop()  # Default action
                print("No valid QR code detected, stopping...")

            cv2.imshow('QR Code Recognition', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        print("Interrupted by user")

    finally:
        cap.release()
        cv2.destroyAllWindows()
        dog.stop()  # Ensure the robot stops
        print("Stopped the robot")

if __name__ == "__main__":
    qr_code_recognition()