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
    dog.stand()
    XGO_edu.SpeechSynthesis("XGO stood tall and ready for an adventure.")
    time.sleep(5)

    # Robot action: Walk forward
    dog.walk(direction=0, speed=50)
    XGO_edu.SpeechSynthesis("XGO started walking through the forest, looking for new friends.")
    time.sleep(5)
    dog.stop()

    # Robot action: Turn left
    dog.turn(direction=-1, speed=50)
    XGO_edu.SpeechSynthesis("Suddenly, XGO heard a noise and turned to the left.")
    time.sleep(2)
    dog.stop()

    # Robot action: Sit down
    dog.sit()
    XGO_edu.SpeechSynthesis("XGO sat down to rest and saw a beautiful butterfly.")
    time.sleep(5)

    # Robot action: Extend arm
    dog.extend_arm()
    XGO_edu.SpeechSynthesis("XGO extended its arm to gently touch the butterfly.")
    time.sleep(5)
    dog.retract_arm()

    # Continue the story
    XGO_edu.SpeechSynthesis("The butterfly flew away, and XGO continued its journey, feeling happy and content.")
    time.sleep(5)

    # End the story
    XGO_edu.SpeechSynthesis("And so, XGO's adventure came to an end, but many more awaited in the future. The end.")
    time.sleep(5)

    dog.lie_down()
    XGO_edu.SpeechSynthesis("XGO lay down to rest, dreaming of new adventures.")
    time.sleep(5)

if __name__ == "__main__":
    interactive_story()