from xgo_sdk import XGO
import time

def trot():
    robot = XGO()

    robot.walk(direction=0, speed=80)
    print("Trotting forward")

    time.sleep(10) # Change this to control how long he will trot for

    robot.stop()
    print("Stopped trotting")

if __name__ == "__main__":
    trot()