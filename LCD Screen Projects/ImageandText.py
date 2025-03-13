from xgoedu import XGOEDU
import time

XGO_edu = XGOEDU()

def display_image():
    print("Displaying an image on the LCD screen...")
    XGO_edu.lcd_picture(0, 0, 'path_to_image.jpg')  # Display an image at position (0, 0)
    time.sleep(5)  # Display for 5 seconds

def display_additional_text():
    print("Displaying additional text on the LCD screen...")
    XGO_edu.lcd_text(10, 200, "This is additional text", 2)  # Display text at position (10, 200) with font size 2
    time.sleep(5)  # Display for 5 seconds

def clear_screen():
    print("Clearing the LCD screen...")
    XGO_edu.lcd_clear()  # Clear the LCD screen

if __name__ == "__main__":
    display_image()
    display_additional_text()
    clear_screen()

    # FOR THIS YOU NEED TO GO TO THE CONFIGURING OF THE RASPBERRY PI SECTION AND FOLLOW IT TO ADD ANY FILES TO THE ROBOT