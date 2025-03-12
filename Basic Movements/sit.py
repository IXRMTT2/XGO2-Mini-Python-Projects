from xgo_sdk import XGO
import time

def sit():
    robot = XGO()

    robot.sit()
    print("Sitting")

    time.sleep(5) # change how long he will stay sat for

    robot.stand()
    print("Standing")

if __name__ == "__main__":
    sit()