from xgoedu import XGOEDU
from xgolib import XGO
import time

# Initialize the AI module and robot
XGO_edu = XGOEDU()
dog = XGO('xgomini')

def interactive_story():
    # Start the story
    XGO_edu.SpeechSynthesis("Once upon a time, in a faraway land, there was a brave robot named XGO.")
    time.sleep(5)

    # Robot action: Stand up
    dog.action(1)  # Assuming action 1 is stand up
    XGO_edu.SpeechSynthesis("XGO stood tall and ready for an adventure.")
    time.sleep(5)

    # Robot action: Walk forward
    dog.move_x(15)  # Move forward
    XGO_edu.SpeechSynthesis("XGO started walking through the forest, looking for new friends.")
    time.sleep(5)
    dog.perform(0)  # Stop

    # Robot action: Turn left
    dog.turn(-100)  # Turn left
    XGO_edu.SpeechSynthesis("Suddenly, XGO heard a noise and turned to the left.")
    time.sleep(2)
    dog.perform(0)  # Stop

    # Robot action: Sit down
    dog.action(2)  # Assuming action 2 is sit down
    XGO_edu.SpeechSynthesis("XGO sat down to rest and saw a beautiful butterfly.")
    time.sleep(5)

    # Robot action: Extend arm
    dog.arm(90, 90)  # Extend arm
    XGO_edu.SpeechSynthesis("XGO extended its arm to gently touch the butterfly.")
    time.sleep(5)
    dog.arm(0, 0)  # Retract arm

    # Continue the story
    XGO_edu.SpeechSynthesis("The butterfly flew away, and XGO continued its journey, feeling happy and content.")
    time.sleep(5)

    # End the story
    XGO_edu.SpeechSynthesis("And so, XGO's adventure came to an end, but many more awaited in the future. The end.")
    time.sleep(5)

    dog.action(3)  # Assuming action 3 is lie down
    XGO_edu.SpeechSynthesis("XGO lay down to rest, dreaming of new adventures.")
    time.sleep(5)

if __name__ == "__main__":
    interactive_story()