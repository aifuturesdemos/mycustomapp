import ast
from flask import Flask, request, jsonify

app = Flask(__name__)

ALLOWED_OPERATIONS = {"sum", "max", "min", "len", "sorted"}


def safe_execute(operation, payload):
    if operation not in ALLOWED_OPERATIONS:
        raise ValueError("Operation not allowed")

    try:
        data = ast.literal_eval(payload)
    except (ValueError, SyntaxError) as exc:
        raise ValueError("Invalid payload format") from exc

    if operation == "sum":
        return sum(data)
    if operation == "max":
        return max(data)
    if operation == "min":
        return min(data)
    if operation == "len":
        return len(data)
    if operation == "sorted":
        return sorted(data)

    raise ValueError("Unsupported operation")


@app.route('/execute', methods=['POST'])
def execute():
    body = request.get_json(silent=True) or {}
    operation = body.get('operation', '')
    payload = body.get('payload', '')

    try:
        result = safe_execute(operation, payload)
        return jsonify({"result": result}), 200
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400


if __name__ == '__main__':
    app.run(debug=False)
