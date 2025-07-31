from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "911 BOT API is Live!"

@app.route('/connect', methods=['POST'])
def connect():
    data = request.get_json()
    login = data.get('login')
    password = data.get('password')
    server = data.get('server')

    # Replace with real MT5 logic later
    if login and password and server:
        return jsonify({"status": "success", "message": f"Connected to {server} as {login}"})
    else:
        return jsonify({"status": "error", "message": "Missing credentials"}), 400
