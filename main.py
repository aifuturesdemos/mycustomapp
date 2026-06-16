import re
import pygame
import sys

# --- Vulnerable Input: Paddle speed from command-line ---
def get_paddle_speed():
    try:
        if len(sys.argv) < 2:
            raise IndexError("No input provided. Please specify paddle speed as a positive integer.")
        user_input = sys.argv[1]
        # Validate input: must be a positive integer
        if not re.fullmatch(r'\d+', user_input):
            raise ValueError("Invalid input: Only positive integers are allowed.")
        paddle_speed = int(user_input)
        if not (1 <= paddle_speed <= 20):
            raise ValueError("Paddle speed must be between 1 and 20.")
        return paddle_speed
    except (IndexError, ValueError) as e:
        print(f"Input error: {e}")
        return 5  # Fallback default
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 5  # Fallback default

# --- Pygame Setup ---
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
paddle_speed = get_paddle_speed()

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
# Input validation, exception handling, and documentation have been added to address security concerns.