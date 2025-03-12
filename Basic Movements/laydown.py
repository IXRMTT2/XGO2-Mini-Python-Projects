from xgo_sdk import XGO
import time

def lay_down():
    robot = XGO()

    robot.lie_down()
    print("Laying down")

    time.sleep(5) # change how long he will stay laid down for

    robot.stand()
    print("Standing")

if __name__ == "__main__":
    lay_down()