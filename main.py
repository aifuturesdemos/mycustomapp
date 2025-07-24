import re
import sys
import argparse

# Secure Input Handling: Use argparse and validate input strictly
parser = argparse.ArgumentParser(description='Paddle speed from command-line')
parser.add_argument('speed', type=int, help='Paddle speed (positive integer)')
args = parser.parse_args()

if args.speed <= 0:
    raise ValueError("Invalid input: Only positive integers are allowed.")
else:
    paddle_speed = args.speed  # Validated input

# ... rest of the game logic remains unchanged ...
