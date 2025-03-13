import time
from xgolib import XGO

dog = XGO('xgomini')

def lay_down():
    print("Laying down...")
    dog.lie_down()  
    time.sleep(5)  # Change how long the robot will stay laid down for

    print("Standing up...")
    dog.stand()  

if __name__ == "__main__":
    lay_down()