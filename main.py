import re
import sys
import logging

# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

# --- Vulnerable Input: Paddle speed from command-line ---
def get_validated_input():
    try:
        if len(sys.argv) < 2:
            raise ValueError("No input provided. Please provide paddle speed as a positive integer.")
        user_input = sys.argv[1]
        # Sanitize input: Only allow positive integers
        if not re.fullmatch(r'\d+', user_input):
            raise ValueError("Invalid input: Only positive integers are allowed.")
        paddle_speed = int(user_input)
        if paddle_speed <= 0:
            raise ValueError("Paddle speed must be a positive integer.")
        return paddle_speed
    except (IndexError, ValueError) as e:
        logging.error(f"Input error: {e}")
        print(f"Error: {e}")
        # Default fallback value
        return 5
    except Exception as e:
        logging.exception("Unexpected error occurred while processing input.")
        print("An unexpected error occurred. Please check the logs.")
        return 5

# --- Pygame Setup ---
import pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Vulnerable Ping Pong (Secured)")

# Game Elements
ball = pygame.Rect(width // 2, height // 2, 15, 15)
ball_speed = [4, 4]
paddle = pygame.Rect(width - 20, height // 2 - 60, 10, 120)

# Main Game Loop
running = True
clock = pygame.time.Clock()
paddle_speed = get_validated_input()

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
