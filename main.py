import re
import pygame
import sys

# --- Secure Input: Paddle speed from command-line ---
def get_secure_paddle_speed():
    """Securely parse paddle speed from command line arguments with proper validation."""
    try:
        if len(sys.argv) < 2:
            return 5  # Default fallback
        
        user_input = sys.argv[1].strip()
        
        # Enhanced validation: check for digits only and reasonable length
        if not user_input.isdigit() or len(user_input) > 3:
            raise ValueError("Invalid input: Only 1-3 digit positive integers allowed")
        
        paddle_speed = int(user_input)
        
        # Bounds checking: reasonable speed limits
        if paddle_speed < 1 or paddle_speed > 50:
            raise ValueError("Paddle speed must be between 1 and 50")
            
        return paddle_speed
        
    except (IndexError, ValueError, TypeError) as e:
        print(f"Warning: {e}. Using default paddle speed.")
        return 5  # Secure fallback default

# Get validated paddle speed
paddle_speed = get_secure_paddle_speed()

# --- Pygame Setup ---
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Secure Ping Pong")

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