import time
from xgolib import XGO

dog = XGO('xgomini')

def extend_and_retract_claw():
    print("Extending arm...")
    dog.extend_arm()  
    time.sleep(2)  # Wait for 2 seconds

    print("Extending claw grip...")
    dog.extend_claw_grip()  
    time.sleep(2)  # Wait for 2 seconds

    print("Retracting claw grip...")
    dog.retract_claw_grip()  
    time.sleep(2)  # Wait for 2 seconds

    print("Retracting arm...")
    dog.retract_arm()  
    time.sleep(2)  # Wait for 2 seconds

    print("Finished extending and retracting claw.")

if __name__ == "__main__":
    extend_and_retract_claw()