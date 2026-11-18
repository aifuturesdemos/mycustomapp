import ast
from flask import Flask, request, jsonify

app = Flask(__name__)

ALLOWED_OPERATIONS = {"add", "subtract", "multiply", "divide"}


def calculate(operation, a, b):
    if operation not in ALLOWED_OPERATIONS:
        raise ValueError("Unsupported operation")

    if operation == "add":
        return a + b
    if operation == "subtract":
        return a - b
    if operation == "multiply":
        return a * b
    if operation == "divide":
        if b == 0:
            raise ValueError("Division by zero")
        return a / b

    raise ValueError("Unsupported operation")


@app.route("/calculate", methods=["POST"])
def safe_calculate():
    data = request.get_json(silent=True) or {}

    operation = data.get("operation")
    a = data.get("a")
    b = data.get("b")

    if operation is None or a is None or b is None:
        return jsonify({"error": "operation, a, and b are required"}), 400

    try:
        a = float(a)
        b = float(b)
        result = calculate(operation, a, b)
        return jsonify({"result": result}), 200
    except (TypeError, ValueError) as exc:
        return jsonify({"error": str(exc)}), 400


@app.route("/parse", methods=["POST"])
def safe_parse():
    data = request.get_json(silent=True) or {}
    value = data.get("value", "")

    try:
        parsed = ast.literal_eval(value)
        return jsonify({"parsed": parsed}), 200
    except (ValueError, SyntaxError):
        return jsonify({"error": "Invalid literal input"}), 400


if __name__ == "__main__":
    app.run(debug=False)
