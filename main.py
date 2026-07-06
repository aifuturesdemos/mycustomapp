import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
DATABASE = "app.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, username FROM users WHERE username = ? AND password = ?",
        (username, password),
    )
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({"message": "Login successful", "user": dict(user)})
    return jsonify({"message": "Invalid credentials"}), 401


if __name__ == '__main__':
    app.run(debug=False)
