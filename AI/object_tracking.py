# color_tracking.py
import cv2
import numpy as np
from xgo_sdk import XGO
import time

def color_tracking():
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

        # Convert the frame to HSV (Hue, Saturation, Value) color space for better color detection
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define the range of the color you want to track (e.g., red)
        # You can adjust these values to track different colors (e.g., blue, green, etc.)
        lower_red = np.array([0, 120, 70])
        upper_red = np.array([10, 255, 255])

        # Create a mask to extract the red object
        mask = cv2.inRange(hsv, lower_red, upper_red)

        # Find contours of the colored object
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            # Find the largest contour (this will be the tracked object)
            largest_contour = max(contours, key=cv2.contourArea)

            # Get the bounding box for the largest contour
            x, y, w, h = cv2.boundingRect(largest_contour)

            # Draw a rectangle around the detected object (colored object)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Calculate the center of the object
            center_x = x + w // 2

            # Move the robot based on the position of the object
            if center_x < 200:  # Object is on the left side of the camera
                robot.turn(direction=-1, speed=50)  # Turn left
                print("Turning left...")
            elif center_x > 440:  # Object is on the right side of the camera
                robot.turn(direction=1, speed=50)  # Turn right
                print("Turning right...")
            else:  # Object is centered
                robot.walk(direction=0, speed=50)  # Move forward
                print("Moving forward...")

        # Display the resulting frame
        cv2.imshow('Color Object Tracking', frame)

        # Break the loop if the user presses 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    color_tracking()


            
