import re
import sys
import argparse
import pygam e

# --- Vulnerable Input: Pad dle speed from command-line ---
def validate_input():
    parser = argparse.ArgumentParser(description='Set paddle speed for the game.')
    parser.add_argument('paddle_speed', type=int, help='Paddle speed (positive integer)')
    args = parser.parse_args()
    if args.paddle_speed <= 0:
        raise ValueError('Invalid input: Only positive integers are allowed.')
    return args.paddle_speed

try:
    paddle_speed = validate_input()
except (IndexError, ValueError, SystemExit):
    paddle_speed = 5  # Fallback default

# --- Pygame Setup ---
pygam e.init()
width, height = 800, 600
screen = pygam e.display.set_mode((width, height))
pygam e.display.set_caption("Vulnerable Ping Pong")

# Game Elements
ball = pygam e.Rect(width // 2, height // 2, 15, 15)
ball_speed = [4, 4]
paddle = pygam e.Rect(width - 20, height // 2 - 60, 10, 120)

# Main Game Loop
running = True
clock = pygam e.time.Clock()

while running:
    for event in pygam e.event.get():
        if event.type == pygam e.QUIT:
            running = False

    # Paddle Movement
    keys = pygam e.key.get_pressed()
    if keys[pygam e.K_UP] and paddle.top > 0:
        paddle.y -= paddle_speed
    if keys[pygam e.K_DOWN] and paddle.bottom < height:
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
    pygam e.draw.ellipse(screen, (255, 255, 255), ball)
    pygam e.draw.rect(screen, (255, 255, 255), paddle)
    pygam e.display.flip()
    clock.tick(60)

pygam e.quit()
