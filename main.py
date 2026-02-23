# main.py (Security Fix)
import os
import re
import logging

logging.basicConfig(level=logging.INFO)

def sanitize_input(user_input):
    # Basic input validation and sanitization
    if not isinstance(user_input, str):
        raise ValueError("Input must be a string.")
    # Remove potentially dangerous characters
    return re.sub(r'[;|&]', '', user_input)

def process_command(user_input):
    try:
        safe_input = sanitize_input(user_input)
        # Avoid using eval, exec, or os.system directly
        # Instead, use subprocess with controlled arguments
        import subprocess
        result = subprocess.run(["echo", safe_input], capture_output=True, text=True)
        logging.info(f"Command output: {result.stdout}")
        return result.stdout
    except Exception as e:
        logging.error(f"Error processing command: {e}")
        return "An error occurred."

if __name__ == "__main__":
    # Sensitive information should be loaded from environment variables
    secret_key = os.getenv("MYAPP_SECRET_KEY", "")
    user_input = input("Enter command: ")
    output = process_command(user_input)
    print(output)
