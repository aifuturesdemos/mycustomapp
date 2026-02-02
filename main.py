import subprocess

def run_command(user_input):
    # Securely execute command using subprocess with argument list
    try:
        result = subprocess.run(["sh", "-c", user_input], check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")

# Example usage
user_input = input("Enter command: ")
run_command(user_input)
