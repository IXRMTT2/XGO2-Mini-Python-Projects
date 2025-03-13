import time
from xgolib import XGO

dog = XGO('xgomini')

def trot():
    print("Trotting forward...")
    dog.walk(direction=0, speed=80)  
    time.sleep(10)  # Change this to control how long the robot will trot for

    dog.stop()  # Stop the robot
    print("Stopped trotting")

if __name__ == "__main__":
    trot()