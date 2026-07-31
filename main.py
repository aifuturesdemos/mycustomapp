import ast
from flask import Flask, request, jsonify

app = Flask(__name__)

ALLOWED_OPERATORS = {
    ast.Add: lambda a, b: a + b,
    ast.Sub: lambda a, b: a - b,
    ast.Mult: lambda a, b: a * b,
    ast.Div: lambda a, b: a / b,
    ast.Mod: lambda a, b: a % b,
    ast.Pow: lambda a, b: a ** b,
    ast.USub: lambda a: -a,
    ast.UAdd: lambda a: +a,
}


def safe_eval(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.Num):
        return node.n
    if isinstance(node, ast.BinOp) and type(node.op) in ALLOWED_OPERATORS:
        left = safe_eval(node.left)
        right = safe_eval(node.right)
        return ALLOWED_OPERATORS[type(node.op)](left, right)
    if isinstance(node, ast.UnaryOp) and type(node.op) in ALLOWED_OPERATORS:
        operand = safe_eval(node.operand)
        return ALLOWED_OPERATORS[type(node.op)](operand)
    raise ValueError("Unsupported expression")


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json(silent=True) or {}
    expression = data.get('expression', '')

    if not isinstance(expression, str) or len(expression) > 100:
        return jsonify({'error': 'Invalid expression'}), 400

    try:
        parsed = ast.parse(expression, mode='eval')
        result = safe_eval(parsed.body)
        return jsonify({'result': result})
    except Exception:
        return jsonify({'error': 'Invalid expression'}), 400


if __name__ == '__main__':
    app.run(debug=False)
