from flask import Flask, jsonify
from prometheus_client import start_http_server, Summary, Counter, generate_latest

app = Flask(__name__)

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
REQUEST_COUNT = Counter('request_count', 'Total request count')

@app.route('/users', methods=['GET'])
@REQUEST_TIME.time()
def get_users():
    REQUEST_COUNT.inc()
    users = [
        {"id": 1, "name": "John Doe"},
        {"id": 2, "name": "Jane Doe"}
    ]
    return jsonify(users)

@app.route('/metrics', methods=['GET'])
def metrics():
    return generate_latest()

if __name__ == '__main__':
    start_http_server(8000)  # Start Prometheus metrics server
    app.run(host='0.0.0.0', port=5000)