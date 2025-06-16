import pygame
import sys

# --- Vulnerable Input: Paddle speed from command-line ---
def get_valid_paddle_speed():
    default_speed = 5
    min_speed = 1
    max_speed = 20
    try:
        if len(sys.argv) > 1:
            arg = sys.argv[1]
            paddle_speed = int(arg)
            if paddle_speed < min_speed or paddle_speed > max_speed:
                print(f"Paddle speed out of bounds ({min_speed}-{max_speed}). Using default: {default_speed}")
                return default_speed
            return paddle_speed
        else:
            return default_speed
    except (IndexError, ValueError):
        print(f"Invalid paddle speed input. Using default: {default_speed}")
        return default_speed

paddle_speed = get_valid_paddle_speed()

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
