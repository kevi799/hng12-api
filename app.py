import os
from datetime import datetime
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.route('/')
def home():
    return 'Welcome to the API!'

@app.route('/api/info', methods=['GET'])
def get_info():
    return jsonify({
        "email": "kelvinmulinge9702@gmail.com",
        "current_datetime": datetime.now().isoformat(),
        "github_url": "https://github.com/kevi799/"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
