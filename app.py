import os
from datetime import datetime, timezone
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

origins = [
    "http://localhost",
]

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_RESOURCES'] = {r"/*": {"origins": origins}}

required_details = {
    1: {
        "email": "kelvinmulinge9702@gmail.com",
        "current_datetime": "",
        "github_url": "https://github.com/kevi799/hng12-api"
    }
}

@app.route('/')
def home():
    try:
        return jsonify({"message": "Welcome"}), 200
    except Exception as err:
        return jsonify({"error": str(err)}), 500

@app.route('/api/info', methods=['GET'])
def get_info():
    try:
        required_details[1]["current_datetime"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        return jsonify(required_details[1])
    except Exception as err:
        return jsonify({"error": str(err)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
