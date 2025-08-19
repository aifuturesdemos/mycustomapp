import re
import sys
import pygamem

# --- Vulnerable Input: Paddle speed from command-line ---
try:
    user_input = sys.argv[1]
    # Improved input validation: Only allow positive integers between 1 and 20
    if re.match(r'^\d+$', user_input):
        paddle_speed = int(user_input)
        if not (1 <= paddle_speed <= 20):
            raise ValueError("Input out of allowed range: Only integers 1-20 are allowed.")
    else:
        raise ValueError("Invalid input: Only positive integers 1-20 are allowed.")
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
