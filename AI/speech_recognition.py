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
                dog.move_x(15)  # Move forward
                print("Moving forward...")
            elif "stop" in command:
                dog.perform(0)  # Stop the robot
                print("Stopping...")
            elif "turn left" in command:
                dog.turn(-100)  # Turn left
                print("Turning left...")
            elif "turn right" in command:
                dog.turn(100)  # Turn right
                print("Turning right...")
            elif "sit" in command:
                dog.action(1)  # Perform sit action
                print("Sitting down...")
            elif "stand" in command:
                dog.action(2)  # Perform stand action
                print("Standing up...")
            else:
                print("Command not recognized.")

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the command.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

if __name__ == "__main__":
    voice_command()