from flask import Flask, jsonify, request
from flask_cors import CORS # Install this
import os

app = Flask(__name__)
CORS(app) # Ye important hai browser errors se bachne ke liye

tasks = [
    {"id": 1, "title": "Setup DevOps Pipeline", "done": False},
    {"id": 2, "title": "Deploy to Production", "done": False}
]

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks, "environment": os.getenv("APP_ENV", "Development")})

# ... baaki code same ...

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
