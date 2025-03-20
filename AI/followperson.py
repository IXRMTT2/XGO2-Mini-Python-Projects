import cv2
from xgoedu import XGOEDU
from xgolib import XGO
import time

XGO_edu = XGOEDU()
dog = XGO('xgomini')

def follow_person():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # Set width
    cap.set(4, 480)  # Set height

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)

            if len(faces) > 0:
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    center_x = x + w // 2

                    if center_x < 200:
                        dog.turn(-100)  # Turn left
                        print("Turning left...")
                    elif center_x > 440:
                        dog.turn(100)  # Turn right
                        print("Turning right...")
                    else:
                        dog.move_x(15)  # Move forward
                        print("Moving forward...")
            else:
                dog.perform(0)  # Stop the robot if no faces are detected
                print("No person detected, stopping...")

            cv2.imshow('Person Detection', frame)

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
    follow_person()