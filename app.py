from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Ye data developer ne sample ke liye dala hai
tasks = [
    {"id": 1, "title": "Setup DevOps Pipeline", "done": False},
    {"id": 2, "title": "Deploy to Production", "done": False}
]

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks, "environment": os.getenv("APP_ENV", "Development")})

@app.route('/api/tasks', methods=['POST'])
def add_task():
    new_task = {"id": len(tasks) + 1, "title": request.json['title'], "done": False}
    tasks.append(new_task)
    return jsonify(new_task), 201

if __name__ == '__main__':
    # Developer ne kaha ki ye 5000 port par chalega
    app.run(host='0.0.0.0', port=5000)