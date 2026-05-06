# [REDACTED] Updated main.py to remove hardcoded secret key and use environment variable instead.
import os

SECRET_KEY = os.environ.get('SECRET_KEY')
# ... rest of the code remains unchanged ...