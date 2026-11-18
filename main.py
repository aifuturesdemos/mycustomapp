import ast


def safe_calculate(expression: str):
    """Safely evaluate simple arithmetic expressions only."""
    allowed_nodes = (
        ast.Expression,
        ast.BinOp,
        ast.UnaryOp,
        ast.Constant,
        ast.Add,
        ast.Sub,
        ast.Mult,
        ast.Div,
        ast.Mod,
        ast.Pow,
        ast.USub,
        ast.UAdd,
        ast.Load,
        ast.FloorDiv,
    )

    tree = ast.parse(expression, mode="eval")
    for node in ast.walk(tree):
        if not isinstance(node, allowed_nodes):
            raise ValueError("Invalid expression")
    return eval(compile(tree, "<safe_calculate>", "eval"), {"__builtins__": {}}, {})


if __name__ == "__main__":
    user_input = input("Enter arithmetic expression: ")
    try:
        print(safe_calculate(user_input))
    except Exception:
        print("Invalid input")
