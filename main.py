import pygamemodule
import sys

# Input validation with sanitization
try:
    user_input = sys.argv[1]
    if user_input.isdigit():
        paddle_speed = int(user_input)
    else:
        raise ValueError("Invalid input: Please provide a numeric value.")
except (IndexError, ValueError):
    paddle_speed = 5  # Default fallback value

# Secure handling of sensitive data
# Placeholder for encryption logic if sensitive data is introduced

# Improved error handling
try:
    pygamemodule.init()
    width, height = 800, 600
    screen = pygamemodule.display.set_mode((width, height))
    pygamemodule.display.set_caption("Secure Pong Game")

    # Game Elements
    ball = pygamemodule.Rect(width // 2, height // 2, 15, 15)
    ball_speed = [4, 4]
    paddle = pygamemodule.Rect(width - 20, height // 2 - 60, 10, 120)

    running = True
    clock = pygamemodule.time.Clock()

    while running:
        for event in pygamemodule.event.get():
            if event.type == pygamemodule.QUIT:
                running = False

        # Paddle Movement
        keys = pygamemodule.key.get_pressed()
        if keys[pygamemodule.K_UP] and paddle.top > 0:
            paddle.y -= paddle_speed
        if keys[pygamemodule.K_DOWN] and paddle.bottom < height:
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
        pygamemodule.draw.ellipse(screen, (255, 255, 255), ball)
        pygamemodule.draw.rect(screen, (255, 255, 255), paddle)
        pygamemodule.display.flip()
        clock.tick(60)

    pygamemodule.quit()
except Exception as e:
    print(f"An error occurred: {e}")