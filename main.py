import re
import pygame
import sys

# --- セキュリティ強化済み入力: パドル速度（1～20、先頭ゼロ禁止） ---
def is_valid_paddle_speed(value):
    return re.match(r'^[1-9][0-9]?$', value) and 1 <= int(value) <= 20

try:
    user_input = sys.argv[1]
    if is_valid_paddle_speed(user_input):
        paddle_speed = int(user_input)
    else:
        raise ValueError("無効な入力: 1～20の整数のみ、先頭ゼロ禁止")
except (IndexError, ValueError):
    paddle_speed = 5  # フォールバックデフォルト

# --- Pygameセットアップ ---
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Vulnerable Ping Pong")

# ゲーム要素
ball = pygame.Rect(width // 2, height // 2, 15, 15)
ball_speed = [4, 4]
paddle = pygame.Rect(width - 20, height // 2 - 60, 10, 120)

# メインゲームループ
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # パドル移動
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and paddle.top > 0:
        paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle.bottom < height:
        paddle.y += paddle_speed

    # ボール移動
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    if ball.top <= 0 or ball.bottom >= height:
        ball_speed[1] *= -1
    if ball.left <= 0 or ball.right >= width:
        ball_speed[0] *= -1
    if ball.colliderect(paddle):
        ball_speed[0] *= -1

    # 描画
    screen.fill((0, 0, 0))
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    pygame.draw.rect(screen, (255, 255, 255), paddle)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
