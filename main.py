import pygame
import sys
import logging

# Set up logging for security-relevant events
logging.basicConfig(filename='game_security.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

def get_valid_paddle_speed():
    try:
        # Validate user input from command-line
        if len(sys.argv) > 1:
            arg = sys.argv[1]
            if not arg.isdigit() or int(arg) <= 0 or int(arg) > 100:
                logging.warning(f'Invalid paddle speed input: {arg}')
                return 5  # fallback default
            return int(arg)
        else:
            return 5  # default value
    except (IndexError, ValueError) as e:
        logging.error(f'Exception in parsing paddle speed: {e}')
        return 5

# --- Vulnerable Input: Paddle speed from command-line (fixed above) ---
paddle_speed = get_valid_paddle_speed()

# --- Pygame Setup ---
try:
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
except Exception as e:
    logging.error(f'Unhandled exception in main game loop: {e}')
    print("An error occurred. Please check the log file for details.")
