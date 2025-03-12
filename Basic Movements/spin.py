from xgo_sdk import XGO
import time

def spin():
    robot = XGO()

    robot.turn(direction=1, speed=50) # Change direction to 0 for anti-clockwise
    print("Spinning")

    time.sleep(5) # Change this to control how long he will spin for

    robot.stop()
    print("Stopped spinning")

if __name__ == "__main__":
    spin()