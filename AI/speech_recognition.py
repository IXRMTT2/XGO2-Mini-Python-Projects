
import speech_recognition as sr
from xgo_sdk import XGO

def voice_command():
    
    robot = XGO()

    
    recognizer = sr.Recognizer()

    
    with sr.Microphone() as source:
        print("Say something!")
        while True:
            
            audio = recognizer.listen(source)

            try:
                
                command = recognizer.recognize_google(audio).lower()
                print(f"Command received: {command}")

                
                if "start" in command:
                    robot.walk(direction=0, speed=50)  
                    print("Walking forward...")
                elif "stop" in command:
                    robot.stop()
                    print("Stopped.")
                elif "left" in command:
                    robot.turn(direction=-1, speed=50)  
                    print("Turning left...")
                elif "right" in command:
                    robot.turn(direction=1, speed=50)  
                    print("Turning right...")
                elif "forward" in command:
                    robot.walk(direction=0, speed=50)  
                    print("Moving forward...")
                elif "backward" in command:
                    robot.walk(direction=180, speed=50)  
                    print("Moving backward...")

            except sr.UnknownValueError:
                print("Could not understand audio.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")

if __name__ == "__main__":
    voice_command()