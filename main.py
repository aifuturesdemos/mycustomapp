import json
from flask import Flask, request, jsonify

app = Flask(__name__)


def parse_user_input(raw_data: str):
    """Safely parse JSON input from untrusted sources."""
    if not raw_data:
        return {}
    try:
        parsed = json.loads(raw_data)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON input")
    if not isinstance(parsed, dict):
        raise ValueError("JSON payload must be an object")
    return parsed


@app.route('/process', methods=['POST'])
def process():
    raw_data = request.data.decode('utf-8')
    try:
        payload = parse_user_input(raw_data)
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

    return jsonify({"status": "ok", "received": payload}), 200


if __name__ == '__main__':
    app.run(debug=False)
