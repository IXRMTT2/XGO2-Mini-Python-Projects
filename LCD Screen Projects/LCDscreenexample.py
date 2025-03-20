from xgoedu import XGOEDU
import time

XGO_edu = XGOEDU()

def display_text():
    print("Displaying text on the LCD screen...")
    XGO_edu.lcd_text(10, 10, "Hello, XGO!", color=(255, 255, 255), fontsize=15)  # Display text at position (10, 10) with font size 15
    time.sleep(5)  # Display for 5 seconds

def display_shapes():
    print("Displaying shapes on the LCD screen...")
    XGO_edu.lcd_circle(60, 60, 30, color=(255, 255, 255), width=2)  # Draw a circle at position (60, 60) with radius 30
    XGO_edu.lcd_rectangle(100, 100, 150, 150, outline=(255, 255, 255), width=2)  # Draw a rectangle from (100, 100) to (150, 150)
    XGO_edu.lcd_line(200, 200, 250, 250, color=(255, 255, 255), width=2)  # Draw a line from (200, 200) to (250, 250)
    time.sleep(5)  # Display for 5 seconds

def clear_screen():
    print("Clearing the LCD screen...")
    XGO_edu.lcd_clear()  # Clear the LCD screen

if __name__ == "__main__":
    display_text()
    display_shapes()
    clear_screen()