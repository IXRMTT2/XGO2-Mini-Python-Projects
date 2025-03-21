from xgoedu import XGOEDU
import time

XGO_edu = XGOEDU()

def draw_shapes_and_text():
    print("Drawing shapes and displaying text on the LCD screen...")
    
    # Draw a circle
    XGO_edu.lcd_circle(50, 50, 30, color=(255, 255, 255), width=2)  # Draw a circle at position (50, 50) with radius 30
    time.sleep(3)
    
    # Draw a rectangle
    XGO_edu.lcd_rectangle(100, 100, 150, 150, outline=(255, 255, 255), width=2)  # Draw a rectangle from (100, 100) to (150, 150)
    time.sleep(3)
    
    # Draw a line
    XGO_edu.lcd_line(200, 200, 250, 250, color=(255, 255, 255), width=2)  # Draw a line from (200, 200) to (250, 250)
    time.sleep(3)
    
    # Draw a rounded rectangle
    XGO_edu.lcd_arc(300, 300, 350, 350, 0, 100, color=(255, 255, 255), width=2)  # Draw an arc from (300, 300) to (350, 350) with radius 20
    time.sleep(3)
    
    # Display text
    XGO_edu.lcd_text(10, 10, "Hello, XGO!", color=(255, 255, 255), fontsize=15)  # Display text at position (10, 10) with font size 15
    time.sleep(5)  # Display for 5 seconds

def clear_screen():
    print("Clearing the LCD screen...")
    XGO_edu.lcd_clear()  # Clear the LCD screen

if __name__ == "__main__":
    draw_shapes_and_text()
    clear_screen()