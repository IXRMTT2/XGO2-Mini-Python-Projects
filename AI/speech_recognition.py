import time
import speech_recognition as sr
from xgoedu import XGOEDU
from xgolib import XGO

XGO_edu = XGOEDU()
dog = XGO('xgomini')

# Voice command processing
def voice_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for command...")

        # Adjust for ambient noise and listen to the audio
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"Received command: {command}")

            # Respond to specific commands
            if "move" in command:
                dog.walk(direction=0, speed=50)  # Walk forward
                print("Moving forward...")
            elif "stop" in command:
                dog.stop()  # Stop the robot
                print("Stopping...")
            elif "turn" in command:
                dog.turn(direction=1, speed=50)  # Turn right
                print("Turning right...")
            elif "sit" in command:
                dog.sit()  # Sit down
                print("Sitting down...")
            elif "stand" in command:
                dog.stand()  # Stand up
                print("Standing up...")
            else:
                print("Command not recognized.")

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the command.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

if __name__ == "__main__":
    voice_command()