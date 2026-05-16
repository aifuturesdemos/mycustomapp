import re
import argparse
import pygamem
import sys

# --- Secure Input Handling with argparse ---
def parse_args():
    parser = argparse.ArgumentParser(description="Vulnerable Ping Pong Game")
    parser.add_argument("speed", type=int, help="Paddle speed (positive integer)")
    args = parser.parse_args()
    if args.speed <= 0:
        parser.error("Paddle speed must be a positive integer.")
    return args.speed

try:
    paddle_speed = parse_args()
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

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
