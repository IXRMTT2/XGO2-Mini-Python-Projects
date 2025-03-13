import time
from xgoedu import XGOEDU
from xgolib import XGO

XGO_edu = XGOEDU()
dog = XGO('xgomini')

def play_audio_and_dance():
    # Play an audio file
    print("Playing audio...")
    XGO_edu.xgoSpeaker('path_to_audio_file.mp3')  # Replace with the actual path to the audio file
    time.sleep(5)  # Wait for the audio to finish playing

    # Perform a dance
    print("Performing dance...")
    dog.action(1)  # Perform the first dance move
    time.sleep(1)
    dog.action(2)  # Perform the second dance move
    time.sleep(1)
    dog.action(3)  # Perform the third dance move
    time.sleep(1)
    dog.action(4)  # Perform the fourth dance move
    time.sleep(1)
    dog.action(5)  # Perform the fifth dance move
    time.sleep(1)

    # Stop the robot
    dog.stop()
    print("Dance finished")

if __name__ == "__main__":
    play_audio_and_dance()