import time
from xgoedu import XGOEDU
from xgolib import XGO

XGO_edu = XGOEDU()
dog = XGO('xgomini')

last_face_time = time.time()

while True:
    face_detected = XGO_edu.face_detect()
    
    if face_detected:
        print("face detected")
        dog.action(9)
        last_face_time = time.time()
    else:
        if time.time() - last_face_time >=7:
            print("no face detected for longer than 7 seconds stopping")
            dog.action(0)
        else:
            print("No face detected, performing three axis turn until no face detected for 7 seconds")
            dog.action(4)
            
time.sleep(0.5)