
import cv2
import numpy as np
from xgo_sdk import XGO
import time

def color_tracking():
    
    robot = XGO()

    
    cap = cv2.VideoCapture(0)

    
    cap.set(3, 640)  
    cap.set(4, 480)  

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
                robot.turn(direction=-1, speed=50)  
                print("Turning left...")
            elif center_x > 440:  
                robot.turn(direction=1, speed=50)  
                print("Turning right...")
            else:  
                robot.walk(direction=0, speed=50)  
                print("Moving forward...")

        
        cv2.imshow('Color Object Tracking', frame)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    color_tracking()


            
