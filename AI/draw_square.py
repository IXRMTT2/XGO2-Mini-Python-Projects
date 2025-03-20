import time
from xgolib import XGO

# You will need paper, and to hold the pen in the claw grip of the robot
# You will need to adjust the time.sleep() values to control the side length of the square
# You will need to adjust the speed values to control the speed of the robot
# You will need to adjust the direction values to control the direction of the robot

dog = XGO('xgomini')

def draw_square():
    # Lower the arm to touch the paper
    dog.arm(90, 90)  # Adjust the arm position
    time.sleep(1)
    dog.claw(128)  # Adjust the claw grip
    time.sleep(1)

    # Draw the square
    for _ in range(4):
        dog.move_x(15)  # Move forward
        time.sleep(2)  # Adjust the time to control the side length
        dog.perform(0)  # Stop
        time.sleep(1)
        dog.turn(100)  # Turn right
        time.sleep(1)
        dog.perform(0)  # Stop
        time.sleep(1)

    # Lift the arm
    dog.claw(0)  # Release the claw grip
    time.sleep(1)
    dog.arm(0, 0)  # Retract the arm
    time.sleep(1)

    print("Finished drawing the square")

if __name__ == "__main__":
    draw_square()