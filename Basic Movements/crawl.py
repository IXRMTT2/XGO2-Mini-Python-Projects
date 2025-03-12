from xgo_sdk import XGO
import time

def crawl():
    robot = XGO()

    robot.move_leg(leg_id=0, angle=-30)
    robot.move_leg(leg_id=1, angle=-30)
    robot.move_leg(leg_id=2, angle=-30)
    robot.move_leg(leg_id=3, angle=-30)
    print("Lowering Legs")

    time.sleep(3) # gives the robot time to lower his legs

    robot.walk(direction=0, speed=30)
    print("Crawling")

    time.sleep(5) # change how long he will crawl for

    robot.stop()
    print("Stopped")

    time.sleep(3) # gives the robot time to stop

    robot.stand()
    print("Standing")

    print(2) # gives the robot time to stand up

if __name__ == "__main__":
    crawl()