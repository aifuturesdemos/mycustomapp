import ast
from flask import Flask, request, jsonify

app = Flask(__name__)

ALLOWED_OPERATIONS = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: a / b if b != 0 else (_ for _ in ()).throw(ValueError("Division by zero")),
}


def parse_number(value):
    if isinstance(value, (int, float)):
        return value
    if isinstance(value, str):
        parsed = ast.literal_eval(value)
        if isinstance(parsed, (int, float)):
            return parsed
    raise ValueError("Operands must be numeric")


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json(silent=True) or {}
    operation = data.get('operation')
    left = data.get('left')
    right = data.get('right')

    if operation not in ALLOWED_OPERATIONS:
        return jsonify({"error": "Unsupported operation"}), 400

    try:
        a = parse_number(left)
        b = parse_number(right)
        result = ALLOWED_OPERATIONS[operation](a, b)
        return jsonify({"result": result})
    except (ValueError, SyntaxError):
        return jsonify({"error": "Invalid numeric input"}), 400


if __name__ == '__main__':
    app.run(debug=False)
