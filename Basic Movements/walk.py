from xgo_sdk import XGO
import time 

def walk():
    robot=XGO()

    robot.walk(direction=0, speed=50)
    print("Executing Walk")

    time.sleep(10) # change this for how long you would like him to walk for

    robot.stop()
    print("Stopped Walking")#

if __name__ == "__main__":
    walk()
