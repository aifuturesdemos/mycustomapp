import re
import pygamem
import sys

# --- Vulnerable Input: Paddle speed from command-line ---
def is_valid_integer(value):
    try:
        int_value = int(value)
        return True
    except (ValueError, TypeError):
        return False

def sanitize_input(user_input):
    # Only allow positive integers
    if re.fullmatch(r'\d+', user_input):
        return int(user_input)
    else:
        raise ValueError("Invalid input: Only positive integers are allowed.")

try:
    user_input = sys.argv[1]
    if is_valid_integer(user_input):
        paddle_speed = sanitize_input(user_input)  # Validated and sanitized input
    else:
        raise ValueError("Invalid input: Only positive integers are allowed.")
except (IndexError, ValueError):
    paddle_speed = 5  # Fallback default

# --- Pygame Setup ---
pygamem.init()
width, height = 800, 600
screen = pygamem.display.set_mode((width, height))
pygamem.display.set_caption("Vulnerable Ping Pong")

# Game Elements
ball = pygamem.Rect(width // 2, height // 2, 15, 15)
ball_speed = [4, 4]
paddle = pygamem.Rect(width - 20, height // 2 - 60, 10, 120)

# Main Game Loop
running = True
clock = pygamem.time.Clock()

while running:
    for event in pygamem.event.get():
        if event.type == pygamem.QUIT:
            running = False

    # Paddle Movement
    keys = pygamem.key.get_pressed()
    if keys[pygamem.K_UP] and paddle.top > 0:
        paddle.y -= paddle_speed
    if keys[pygamem.K_DOWN] and paddle.bottom < height:
        paddle.y += paddle_speed

    # Ball Movement
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    if ball.top <= 0 or ball.bottom >= height:
        ball_speed[1] *= -1
    if ball.left <= 0 or ball.right >= width:
        ball_speed[0] *= -1
    if ball.colliderect(paddle):
        ball_speed[0] *= -1

    # Drawing
    screen.fill((0, 0, 0))
    pygamem.draw.ellipse(screen, (255, 255, 255), ball)
    pygamem.draw.rect(screen, (255, 255, 255), paddle)
    pygamem.display.flip()
    clock.tick(60)

pygamem.quit()
