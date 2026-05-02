# Updated main.py to remove hardcoded credentials and use environment variables instead
import os

# Before: username = 'admin'
#         password = 'password123'
username = os.environ.get('APP_USERNAME')
password = os.environ.get('APP_PASSWORD')

def authenticate(user, pwd):
    return user == username and pwd == password

if __name__ == "__main__":
    input_user = input("Username: ")
    input_pwd = input("Password: ")
    if authenticate(input_user, input_pwd):
        print("Access granted.")
    else:
        print("Access denied.")
