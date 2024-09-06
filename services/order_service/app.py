from flask import Flask, jsonify, request
from prometheus_client import start_http_server, Summary, Counter, generate_latest
import logging
import requests
from retrying import retry
import pybreaker

user_service_breaker = pybreaker.CircuitBreaker(fail_max=3, reset_timeout=30)

@user_service_breaker
@retry(stop_max_attempt_number=3, wait_fixed=1000)
def get_user(user_id):
    response = requests.get(f'http://user_service:5001/users/{user_id}')
    response.raise_for_status()
    return response.json()

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
REQUEST_COUNT = Counter('request_count', 'Total request count')

@app.route('/orders', methods=['GET'])
@REQUEST_TIME.time()
def get_orders():
    app.logger.debug("Handling /orders request")
    REQUEST_COUNT.inc()
    orders = [
        {"id": 1, "user_id": 1, "product": "Book"},
        {"id": 2, "user_id": 2, "product": "Laptop"}
    ]
    return jsonify(orders)

@app.route('/create_order', methods=['POST'])
@REQUEST_TIME.time()
def create_order():
    app.logger.debug("Handling /create_order request")
    REQUEST_COUNT.inc()
    order_data = request.json
    user_id = order_data.get('user_id')
    
    try:
        user = get_user(user_id)
        new_order = {"id": 3, "user_id": user_id, "product": order_data.get('product')}
        return jsonify(new_order), 201
    except requests.HTTPError as e:
        if e.response.status_code == 404:
            return jsonify({"error": "User not found"}), 404
        return jsonify({"error": "User service error"}), 500
    except requests.RequestException:
        return jsonify({"error": "User service unavailable"}), 503

@app.route('/metrics', methods=['GET'])
def metrics():
    return generate_latest()


@app.route('/', methods=['GET'])
def index():
    return "Order Service is running!"

if __name__ == '__main__':
    from waitress import serve
    start_http_server(8001)  
    serve(app, host='0.0.0.0', port=5002)  
