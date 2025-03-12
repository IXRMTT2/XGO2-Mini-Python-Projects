# voice_command.py
import speech_recognition as sr
from xgo_sdk import XGO

def voice_command():
    # Initialize the XGO-Mini robot
    robot = XGO()

    # Initialize the recognizer for speech recognition
    recognizer = sr.Recognizer()

    # Create a microphone object
    with sr.Microphone() as source:
        print("Say something!")
        while True:
            # Listen for audio input
            audio = recognizer.listen(source)

            try:
                # Use Google's speech recognition to convert speech to text
                command = recognizer.recognize_google(audio).lower()
                print(f"Command received: {command}")

                # Control robot based on voice command
                if "start" in command:
                    robot.walk(direction=0, speed=50)  # Walk forward
                    print("Walking forward...")
                elif "stop" in command:
                    robot.stop()
                    print("Stopped.")
                elif "left" in command:
                    robot.turn(direction=-1, speed=50)  # Turn left
                    print("Turning left...")
                elif "right" in command:
                    robot.turn(direction=1, speed=50)  # Turn right
                    print("Turning right...")
                elif "forward" in command:
                    robot.walk(direction=0, speed=50)  # Move forward
                    print("Moving forward...")
                elif "backward" in command:
                    robot.walk(direction=180, speed=50)  # Move backward
                    print("Moving backward...")

            except sr.UnknownValueError:
                print("Could not understand audio.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")

if __name__ == "__main__":
    voice_command()