import time
from xgolib import XGO

dog = XGO('xgomini')

def sit():
    print("Sitting...")
    dog.sit()  # Assuming this method makes the robot sit
    time.sleep(5)  # Change how long the robot will stay sat for

    print("Standing up...")
    dog.stand()  # Assuming this method makes the robot stand up

if __name__ == "__main__":
    sit()