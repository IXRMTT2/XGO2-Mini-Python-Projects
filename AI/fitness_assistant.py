import cv2
from xgoedu import XGOEDU
from xgolib import XGO
import time

# Initialize the AI module and robot
XGO_edu = XGOEDU()
dog = XGO('xgomini')

def fitness_trainer():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # Set width
    cap.set(4, 480)  # Set height

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            pose = XGO_edu.posnetRecognition(frame)
            print(f"Detected pose: {pose}")

            if pose == "tree_pose":
                dog.action(1)  # Perform an action for tree pose
                XGO_edu.SpeechSynthesis("Great job! Hold the tree pose.")
                print("Great job! Hold the tree pose.")
            elif pose == "warrior_pose":
                dog.action(2)  # Perform an action for warrior pose
                XGO_edu.SpeechSynthesis("Excellent! Keep holding the warrior pose.")
                print("Excellent! Keep holding the warrior pose.")
            elif pose == "downward_dog":
                dog.action(3)  # Perform an action for downward dog pose
                XGO_edu.SpeechSynthesis("Nice! Hold the downward dog pose.")
                print("Nice! Hold the downward dog pose.")
            else:
                dog.action(0)  # Default action
                XGO_edu.SpeechSynthesis("Please get into a recognized pose.")
                print("Please get into a recognized pose.")

            cv2.imshow('Fitness Trainer', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        print("Interrupted by user")

    finally:
        cap.release()
        cv2.destroyAllWindows()
        dog.stop()  # Ensure the robot stops
        print("Stopped the robot")

if __name__ == "__main__":
    fitness_trainer()