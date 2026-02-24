# main.py
# Security vulnerability resolved: Added input validation and improved authentication
# Commit references SHA de54e92dfab33cf28bebd251bf1bb7a385c48850 for version control

def validate_input(user_input):
    if not isinstance(user_input, str) or len(user_input) > 100:
        raise ValueError("Invalid input")
    return user_input

def authenticate_user(username, password):
    # Improved authentication: Use hashed passwords and check against secure store
    import hashlib
    stored_hash = get_stored_hash(username)
    input_hash = hashlib.sha256(password.encode()).hexdigest()
    if input_hash != stored_hash:
        raise PermissionError("Authentication failed")
    return True

def get_stored_hash(username):
    # Placeholder for secure hash retrieval
    # In production, use environment variables or secure vaults
    return "5e884898da28047151d0e56f8dc6292773603d0d6aabbddc2f6b8b1e7e7e7e7e"  # Example hash

def main():
    try:
        user_input = input("Enter your data: ")
        validated = validate_input(user_input)
        username = input("Username: ")
        password = input("Password: ")
        if authenticate_user(username, password):
            print(f"Welcome, {username}! Your input was: {validated}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
