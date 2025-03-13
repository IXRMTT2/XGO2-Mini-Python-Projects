import cv2
import numpy as np
from xgoedu import XGOEDU
from xgolib import XGO
import time

# Initialize the AI module and robot
XGO_edu = XGOEDU()
dog = XGO('xgomini')

def detect_and_pickup_red_ball():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # Set width
    cap.set(4, 480)  # Set height

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # Define the range for the color red
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

                if w * h > 5000:  # If the ball is close enough
                    dog.stop()
                    print("Picking up the ball...")
                    dog.extend_arm()
                    time.sleep(1)
                    dog.extend_claw_grip()
                    time.sleep(1)
                    dog.retract_arm()
                    time.sleep(1)
                    print("Holding the ball for 10 seconds...")
                    time.sleep(10)
                    print("Releasing the ball...")
                    dog.extend_arm()
                    time.sleep(1)
                    dog.retract_claw_grip()
                    time.sleep(1)
                    dog.retract_arm()
                    time.sleep(1)
                    print("Returning to normal state...")
                    dog.stop()
                    break

            cv2.imshow('Red Ball Detection', frame)

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
    detect_and_pickup_red_ball()