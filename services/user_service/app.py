from flask import Flask, jsonify
from prometheus_client import start_http_server, Summary, Counter, generate_latest
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
REQUEST_COUNT = Counter('request_count', 'Total request count')

@app.route('/users', methods=['GET'])
@REQUEST_TIME.time()
def get_users():
    app.logger.debug("Handling /users request")
    REQUEST_COUNT.inc()
    users = [
        {"id": 1, "name": "John Doe"},
        {"id": 2, "name": "Jane Doe"}
    ]
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
@REQUEST_TIME.time()
def get_user(user_id):
    app.logger.debug(f"Handling /users/{user_id} request")
    REQUEST_COUNT.inc()
    users = [
        {"id": 1, "name": "John Doe"},
        {"id": 2, "name": "Jane Doe"}
    ]
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/metrics', methods=['GET'])
def metrics():
    return generate_latest()

@app.route('/', methods=['GET'])
def index():
    return "User Service is running!"

if __name__ == '__main__':
    from waitress import serve
    start_http_server(8000)  
    serve(app, host='0.0.0.0', port=5001)