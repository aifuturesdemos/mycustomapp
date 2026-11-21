import html
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return '''
    <h2>Welcome to My Custom App</h2>
    <form action="/greet" method="get">
        <label for="name">Enter your name:</label>
        <input type="text" id="name" name="name">
        <input type="submit" value="Greet Me">
    </form>
    '''


@app.route('/greet')
def greet():
    name = request.args.get('name', '')
    safe_name = html.escape(name, quote=True)
    return f"<h3>Hello, {safe_name}!</h3>"


@app.route('/health')
def health():
    return jsonify({"status": "ok"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
