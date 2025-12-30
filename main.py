import re
import pygame
import sys

# --- Secure Input: Paddle speed from command-line ---
MIN_PADDLE_SPEED = 1
MAX_PADDLE_SPEED = 20
DEFAULT_PADDLE_SPEED = 5

try:
    user_input = sys.argv[1]
    if re.match(r'^\d+$', user_input):
        paddle_speed = int(user_input)
        if not (MIN_PADDLE_SPEED <= paddle_speed <= MAX_PADDLE_SPEED):
            print(f"Invalid input: Paddle speed must be between {MIN_PADDLE_SPEED} and {MAX_PADDLE_SPEED}. Using default value {DEFAULT_PADDLE_SPEED}.")
            paddle_speed = DEFAULT_PADDLE_SPEED
    else:
        print(f"Invalid input: Only positive integers are allowed. Using default value {DEFAULT_PADDLE_SPEED}.")
        paddle_speed = DEFAULT_PADDLE_SPEED
except (IndexError, ValueError):
    paddle_speed = DEFAULT_PADDLE_SPEED  # Fallback default

# --- Pygame Setup ---
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Vulnerable Ping Pong")

# Game Elements
ball = pygame.Rect(width // 2, height // 2, 15, 15)
ball_speed = [4, 4]
paddle = pygame.Rect(width - 20, height // 2 - 60, 10, 120)

# Main Game Loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and paddle.top > 0:
        paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle.bottom < height:
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
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    pygame.draw.rect(screen, (255, 255, 255), paddle)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
