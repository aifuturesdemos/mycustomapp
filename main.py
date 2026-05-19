# Refactored main.py to fix SQL injection vulnerability
# Original code:
# query = f"SELECT * FROM users WHERE username = '{user_input}'"
# Fixed code:
import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
query = "SELECT * FROM users WHERE username = ?"
cursor.execute(query, (user_input,))
# This change uses parameterized queries to prevent SQL injection.
