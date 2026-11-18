import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

ALLOWED_COMMANDS = {
    "date": ["date"],
    "uptime": ["uptime"],
    "whoami": ["whoami"],
}


@app.route("/run", methods=["POST"])
def run_command():
    data = request.get_json(silent=True) or {}
    command = data.get("command", "")

    if command not in ALLOWED_COMMANDS:
        return jsonify({"error": "invalid command"}), 400

    try:
        result = subprocess.run(
            ALLOWED_COMMANDS[command],
            capture_output=True,
            text=True,
            check=False,
            timeout=5,
        )
        return jsonify(
            {
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode,
            }
        )
    except subprocess.TimeoutExpired:
        return jsonify({"error": "command timed out"}), 504


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
