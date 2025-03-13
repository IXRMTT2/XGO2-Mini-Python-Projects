import time
from xgolib import XGO

# You will need paper, and to hold the pen in the claw grip of the robot
# You will need to adjust the time.sleep() values to control the side length of the square
# You will need to adjust the speed values to control the speed of the robot
# You will need to adjust the direction values to control the direction of the robot

dog = XGO('xgomini')

def draw_square():
    # Lower the arm to touch the paper
    dog.extend_arm()
    time.sleep(1)
    dog.extend_claw_grip()
    time.sleep(1)

    # Draw the square
    for _ in range(4):
        dog.walk(direction=0, speed=20)  # Move forward
        time.sleep(2)  # Adjust the time to control the side length
        dog.stop()
        time.sleep(1)
        dog.turn(direction=1, speed=50)  # Turn right
        time.sleep(1)
        dog.stop()
        time.sleep(1)

    # Lift the arm
    dog.retract_claw_grip()
    time.sleep(1)
    dog.retract_arm()
    time.sleep(1)

    print("Finished drawing the square")

if __name__ == "__main__":
    draw_square()