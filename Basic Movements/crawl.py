import time
from xgoedu import XGOEDU
from xgolib import XGO

XGO_edu = XGOEDU()
dog = XGO('xgomini')
def crawl():
    print("Starting to crawl...")
    
    dog.lower_body()  
    time.sleep(1)
 
    dog.walk(direction=0, speed=50)  # Move forward at walking speed
    time.sleep(3)  # Crawl for 3 seconds
    dog.stop()  # Stop the robot
    print("Finished crawling.")

if __name__ == "__main__":
    crawl()