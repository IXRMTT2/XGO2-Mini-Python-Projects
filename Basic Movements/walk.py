import time
from xgolib import XGO

dog = XGO('xgomini')

def walk():
    try:
        print("Walking forward...")
        dog.walk(direction=0, speed=50)  # Walk forward
        time.sleep(10)  # Change this to control how long the robot will walk for

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        dog.stop()  # Stop the robot
        print("Stopped walking")

if __name__ == "__main__":
    walk()
