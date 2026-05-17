# Updated main.py to remove hardcoded credentials and use environment variables instead
import os

# Instead of hardcoded credentials like:
# username = 'admin'
# password = 'password123'

username = os.getenv('APP_USERNAME')
password = os.getenv('APP_PASSWORD')

if not username or not password:
    raise ValueError('Missing required environment variables for credentials.')

# Rest of the application logic remains unchanged
