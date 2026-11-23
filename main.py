import ast
import os


def safe_parse_literal(user_input: str):
    """Safely parse Python literal input without executing code."""
    try:
        return ast.literal_eval(user_input)
    except (ValueError, SyntaxError) as exc:
        raise ValueError("Invalid literal input") from exc


def handle_input(user_input: str):
    parsed = safe_parse_literal(user_input)
    return {"status": "ok", "data": parsed}


if __name__ == "__main__":
    raw = os.environ.get("APP_INPUT", "'default'")
    result = handle_input(raw)
    print(result)
