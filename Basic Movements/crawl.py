import time
from xgoedu import XGOEDU
from xgolib import XGO

# Initialize the AI module and robot movement
XGO_edu = XGOEDU()
dog = XGO('xgomini')

# Crawl motion (lower body, then walk forward)
def crawl():
    print("Starting to crawl...")
    
    # Lower the body to a crawling position (if the robot supports this)
    # Assuming the XGO-Mini can perform body lowering for crawling (you may need to adjust this based on actual capabilities)
    dog.lower_body()  # This is a placeholder. Actual function might be different.
    time.sleep(1)
    
    # Walk forward after lowering the body
    dog.walk(direction=0, speed=50)  # Move forward at walking speed
    time.sleep(3)  # Crawl for 3 seconds
    dog.stop()  # Stop the robot
    print("Finished crawling.")

if __name__ == "__main__":
    crawl()