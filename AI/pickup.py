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
                    dog.turn(-100)  # Turn left
                    print("Turning left...")
                elif center_x > 440:
                    dog.turn(100)  # Turn right
                    print("Turning right...")
                else:
                    dog.move_x(15)  # Move forward
                    print("Moving forward...")

                if w * h > 5000:  # If the ball is close enough
                    dog.perform(0)  # Stop
                    print("Picking up the ball...")
                    dog.arm(90, 90)  # Extend arm
                    time.sleep(1)
                    dog.claw(128)  # Grip claw
                    time.sleep(1)
                    dog.arm(0, 0)  # Retract arm
                    time.sleep(1)
                    print("Holding the ball for 10 seconds...")
                    time.sleep(10)
                    print("Releasing the ball...")
                    dog.arm(90, 90)  # Extend arm
                    time.sleep(1)
                    dog.claw(0)  # Release claw
                    time.sleep(1)
                    dog.arm(0, 0)  # Retract arm
                    time.sleep(1)
                    print("Returning to normal state...")
                    dog.perform(0)  # Stop
                    break

            cv2.imshow('Red Ball Detection', frame)

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
    detect_and_pickup_red_ball()