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

                if x < 200:
                    dog.turn(direction=-1, speed=50)  # Turn left
                elif x > 440:
                    dog.turn(direction=1, speed=50)  # Turn right
                else:
                    dog.walk(direction=0, speed=50)  # Walk forward

        cv2.imshow('Face Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    face_detection()