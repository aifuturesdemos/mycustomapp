import ast
from flask import Flask, request, jsonify

app = Flask(__name__)

ALLOWED_OPERATIONS = {"add", "subtract", "multiply"}


def safe_parse_payload(raw_value):
    try:
        parsed = ast.literal_eval(raw_value)
    except (ValueError, SyntaxError):
        raise ValueError("Invalid payload format")

    if not isinstance(parsed, dict):
        raise ValueError("Payload must be a dictionary")

    operation = parsed.get("operation")
    a = parsed.get("a")
    b = parsed.get("b")

    if operation not in ALLOWED_OPERATIONS:
        raise ValueError("Operation not allowed")

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Operands must be numeric")

    return operation, a, b


@app.route("/calculate", methods=["POST"])
def calculate():
    raw_payload = request.form.get("payload", "")

    try:
        operation, a, b = safe_parse_payload(raw_payload)
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    else:
        result = a * b

    return jsonify({"result": result}), 200


if __name__ == "__main__":
    app.run(debug=False)
