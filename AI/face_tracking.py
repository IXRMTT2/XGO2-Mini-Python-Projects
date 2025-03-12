# face_detection.py
import cv2
from xgo_sdk import XGO
import time

def face_detection():
    # Initialize the XGO-Mini robot
    robot = XGO()

    # Initialize OpenCV and the camera
    cap = cv2.VideoCapture(0)

    # Set the width and height of the camera feed
    cap.set(3, 640)  # width
    cap.set(4, 480)  # height

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to grayscale for easier face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Load Haar Cascade for face detection
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # If faces are detected, react to them
        if len(faces) > 0:
            for (x, y, w, h) in faces:
                # Draw a rectangle around the face
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                # Move the robot to face the detected face (simplified logic)
                if x < 200:
                    robot.turn(direction=-1, speed=50)  # Turn left
                elif x > 440:
                    robot.turn(direction=1, speed=50)  # Turn right
                else:
                    robot.walk(direction=0, speed=50)  # Move forward

        # Show the camera feed with face detection
        cv2.imshow('Face Detection', frame)

        # Stop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release camera and close OpenCV window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    face_detection()