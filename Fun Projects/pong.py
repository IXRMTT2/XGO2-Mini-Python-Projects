import time
import random
from xgoedu import XGOEDU

XGO_edu = XGOEDU()

# Screen dimensions
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 240

# Paddle dimensions
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50

# Ball dimensions
BALL_SIZE = 10

# Paddle positions
player_paddle_y = (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2
ai_paddle_y = (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2

# Ball position and velocity
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_dx = 3
ball_dy = 3

def draw_paddle(x, y):
    XGO_edu.lcd_rectangle(x, y, x + PADDLE_WIDTH, y + PADDLE_HEIGHT)

def draw_ball(x, y):
    XGO_edu.lcd_rectangle(x, y, x + BALL_SIZE, y + BALL_SIZE)

def clear_screen():
    XGO_edu.lcd_clear()

def update_paddle_position(paddle_y, dy):
    paddle_y += dy
    if paddle_y < 0:
        paddle_y = 0
    elif paddle_y > SCREEN_HEIGHT - PADDLE_HEIGHT:
        paddle_y = SCREEN_HEIGHT - PADDLE_HEIGHT
    return paddle_y

def pong_game():
    global player_paddle_y, ai_paddle_y, ball_x, ball_y, ball_dx, ball_dy

    try:
        while True:
            clear_screen()

            # Draw paddles and ball
            draw_paddle(10, player_paddle_y)
            draw_paddle(SCREEN_WIDTH - 20, ai_paddle_y)
            draw_ball(ball_x, ball_y)

            # Update ball position
            ball_x += ball_dx
            ball_y += ball_dy

            # Ball collision with top and bottom
            if ball_y <= 0 or ball_y >= SCREEN_HEIGHT - BALL_SIZE:
                ball_dy = -ball_dy

            # Ball collision with paddles
            if (ball_x <= 20 and player_paddle_y <= ball_y <= player_paddle_y + PADDLE_HEIGHT) or \
               (ball_x >= SCREEN_WIDTH - 30 and ai_paddle_y <= ball_y <= ai_paddle_y + PADDLE_HEIGHT):
                ball_dx = -ball_dx

            # Ball out of bounds
            if ball_x < 0 or ball_x > SCREEN_WIDTH:
                ball_x = SCREEN_WIDTH // 2
                ball_y = SCREEN_HEIGHT // 2
                ball_dx = random.choice([-3, 3])
                ball_dy = random.choice([-3, 3])

            # Update AI paddle position
            if ball_y > ai_paddle_y + PADDLE_HEIGHT // 2:
                ai_paddle_y = update_paddle_position(ai_paddle_y, 3)
            elif ball_y < ai_paddle_y + PADDLE_HEIGHT // 2:
                ai_paddle_y = update_paddle_position(ai_paddle_y, -3)

            # Update player paddle position (for simplicity, player paddle is stationary in this example)
            # You can add code to control the player paddle using buttons or other input methods

            time.sleep(0.05)

    except KeyboardInterrupt:
        print("Game interrupted by user")

    finally:
        clear_screen()
        print("Game over")

if __name__ == "__main__":
    pong_game()