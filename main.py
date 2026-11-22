import ast
from flask import Flask, request, jsonify

app = Flask(__name__)

ALLOWED_OPERATIONS = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: a / b if b != 0 else (_ for _ in ()).throw(ValueError("division by zero")),
}


def parse_number(value):
    if isinstance(value, (int, float)):
        return value
    if isinstance(value, str):
        parsed = ast.literal_eval(value)
        if isinstance(parsed, (int, float)):
            return parsed
    raise ValueError("invalid numeric input")


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json(silent=True) or {}
    operation = data.get("operation")
    a = data.get("a")
    b = data.get("b")

    if operation not in ALLOWED_OPERATIONS:
        return jsonify({"error": "unsupported operation"}), 400

    try:
        left = parse_number(a)
        right = parse_number(b)
        result = ALLOWED_OPERATIONS[operation](left, right)
        return jsonify({"result": result}), 200
    except (ValueError, SyntaxError):
        return jsonify({"error": "invalid input"}), 400


if __name__ == "__main__":
    app.run(debug=False)
