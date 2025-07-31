from flask import Flask, request, jsonify
from flask_cors import CORS  # <-- Add this import

app = Flask(__name__)
CORS(app)  # <-- Enable CORS for your Flask app

@app.route('/')
def index():
    return '911 BOT API is running ✅'

@app.route('/connect', methods=['POST'])
def connect():
    data = request.json
    login = data.get('login')
    password = data.get('password')
    server = data.get('server')
    pair = data.get('pair')
    mode = data.get('mode')
    strategy = data.get('strategy')

    # Just a placeholder response (actual MT5 logic comes later)
    if not all([login, password, server]):
        return jsonify({"success": False, "message": "Missing credentials"}), 400

    print(f"Received credentials: {login} | {password} | {server}")
    print(f"Pair: {pair}, Mode: {mode}, Strategy: {strategy}")

    return jsonify({
        "success": True,
        "message": "Credentials received",
        "data": {
            "login": login,
            "server": server,
            "pair": pair,
            "mode": mode,
            "strategy": strategy
        }
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
