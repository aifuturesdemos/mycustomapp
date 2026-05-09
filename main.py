# Updated main.py with hardcoded credentials removed and replaced by environment variables
import os

# Example: Instead of hardcoding credentials, use environment variables
# OLD: username = "admin"
# OLD: password = "supersecret"
username = os.getenv("APP_USERNAME")
password = os.getenv("APP_PASSWORD")

def authenticate(user, pwd):
    return user == username and pwd == password

if __name__ == "__main__":
    input_user = input("Username: ")
    input_pwd = input("Password: ")
    if authenticate(input_user, input_pwd):
        print("Access granted.")
    else:
        print("Access denied.")
