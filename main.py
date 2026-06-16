# Updated main.py to remove hardcoded credentials and use environment variables for database access
import os
import pygame
import sys
import re

def get_db_connection():
    db_host = os.environ.get('DB_HOST')
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')
    db_name = os.environ.get('DB_NAME')
    if not all([db_host, db_user, db_password, db_name]):
        raise ValueError('Database credentials are not fully set in environment variables.')
    # Example: connect to your database here using the above variables
    # conn = psycopg2.connect(host=db_host, user=db_user, password=db_password, dbname=db_name)
    # return conn

# --- Vulnerable Input: Paddle speed from command-line ---
try:
    user_input = sys.argv[1]
    if re.match(r'^\d+$', user_input):
        paddle_speed = int(user_input)  # Validated input
    else:
        raise ValueError("Invalid input: Only positive integers are allowed.")
except (IndexError, ValueError):
    paddle_speed = 5  # Fallback default

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