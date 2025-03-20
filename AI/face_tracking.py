import cv2
import time
from xgolib import XGO
from xgoedu import XGOEDU

dog = XGO('xgomini')
XGO_edu = XGOEDU()

def face_detection():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # Set width
    cap.set(4, 480)  # Set height

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

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

        cv2.imshow('Face Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    dog.perform(0)  # Ensure the robot stops
    print("Stopped the robot")

if __name__ == "__main__":
    face_detection()