import re
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

SAFE_NAME_PATTERN = re.compile(r'^[A-Za-z0-9_.-]+$')


def validate_name(value: str) -> str:
    if not value or not SAFE_NAME_PATTERN.fullmatch(value):
        raise ValueError("Invalid input. Only letters, numbers, underscore, dash, and dot are allowed.")
    return value


@app.route('/ping', methods=['GET'])
def ping():
    host = request.args.get('host', '')
    try:
        safe_host = validate_name(host)
    except ValueError as exc:
        return jsonify({'error': str(exc)}), 400

    result = subprocess.run(
        ['ping', '-c', '1', safe_host],
        capture_output=True,
        text=True,
        check=False,
        timeout=5,
    )

    return jsonify({
        'stdout': result.stdout,
        'stderr': result.stderr,
        'returncode': result.returncode,
    })


if __name__ == '__main__':
    app.run(debug=False)
