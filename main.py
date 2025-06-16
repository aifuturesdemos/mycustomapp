import sys

try:
    paddle_speed = int(sys.argv[1])
    if paddle_speed < 0 or paddle_speed > 100:
        raise ValueError("Invalid paddle speed. Must be between 0 and 100.")
except (IndexError, ValueError):
    paddle_speed = 5

print(f"Paddle speed set to: {paddle_speed}")