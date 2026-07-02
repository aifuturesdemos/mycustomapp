from flask import Flask, request
import subprocess
import re

app = Flask(__name__)

HOST_PATTERN = re.compile(r'^[A-Za-z0-9.-]+$')

@app.route('/ping')
def ping():
    host = request.args.get('host', '')
    if not host or not HOST_PATTERN.fullmatch(host):
        return 'Invalid host', 400
    result = subprocess.check_output(['ping', '-c', '1', host], text=True)
    return result

if __name__ == '__main__':
    app.run(debug=True)
