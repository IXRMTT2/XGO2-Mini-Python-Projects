import cv2
import numpy as np
from xgolib import XGO
import time

def color_tracking():
    dog = XGO('xgomini')

    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # Set width
    cap.set(4, 480)  # Set height

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            lower_red = np.array([0, 120, 70])
            upper_red = np.array([10, 255, 255])

            mask = cv2.inRange(hsv, lower_red, upper_red)

            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if contours:
                largest_contour = max(contours, key=cv2.contourArea)
                x, y, w, h = cv2.boundingRect(largest_contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                center_x = x + w // 2

                if center_x < 200:  
                    dog.turn(direction=-1, speed=50)  # Turn left
                    print("Turning left...")
                elif center_x > 440:  
                    dog.turn(direction=1, speed=50)  # Turn right
                    print("Turning right...")
                else:  
                    dog.walk(direction=0, speed=50)  # Move forward
                    print("Moving forward...")

            cv2.imshow('Color Object Tracking', frame)

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
    color_tracking()



