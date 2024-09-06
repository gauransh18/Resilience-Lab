from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def health():
    user_health = check_service_health('http://user_service:5001')
    order_health = check_service_health('http://order_service:5002')
    return jsonify({
        'user_service': user_health,
        'order_service': order_health
    })

def check_service_health(url):
    try:
        response = requests.get(url, timeout=5)
        return 'healthy' if response.status_code == 200 else 'unhealthy'
    except requests.RequestException:
        return 'unhealthy'

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=8080)