import time
from xgolib import XGO

dog = XGO('xgomini')

def spin():
    print("Spinning...")
    dog.turn(direction=1, speed=50)  
    time.sleep(5)  # Change how long the robot will spin for

    dog.stop()  # Stop the robot
    print("Stopped")

if __name__ == "__main__":
    spin()