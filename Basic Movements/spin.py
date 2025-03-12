from xgo_sdk import XGO
import time

def spin():
    robot = XGO()

    robot.turn(direction=1, speed=50)
    print("Spinning")

    time.sleep(5) # change how long he will spin for

    robot.stop()
    print("Stopped")

if __name__ == "__main__":
    spin()