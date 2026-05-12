# main.py (fixed)
import os

# Instead of hardcoded credentials, use environment variables
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

# Example usage
if not DB_USER or not DB_PASSWORD:
    raise ValueError('Database credentials are not set in environment variables.')

# ... rest of the application logic ...
