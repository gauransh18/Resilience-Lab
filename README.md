# Resilient Microservices Demo

## About the Project

This project demonstrates a resilient microservices architecture with a focus on observability, fault tolerance, and chaos engineering. It consists of two main services (User Service and Order Service), a dashboard, and supporting infrastructure for monitoring and logging.

Key features:
- Microservices built with Flask
- Docker containerization
- Prometheus monitoring
- Fluentd and Elasticsearch for logging
- Circuit breaker and retry mechanisms
- Basic chaos testing
- Simple web dashboard for service health monitoring

## Services

1. User Service: Manages user data
2. Order Service: Handles order processing and interacts with User Service
3. Dashboard: Provides a web interface to monitor service health

## Prerequisites

- Docker and Docker Compose
- Python 3.8+

## Getting Started

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <project-directory>
   ```

2. Build and start the services:
   ```
   docker-compose up --build -d
   ```

3. Access the services:
   - Dashboard: http://localhost:8080
   - User Service: http://localhost:5001
   - Order Service: http://localhost:5002

## Monitoring

- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000 (if configured)

## Logging

Logs are collected using Fluentd and stored in Elasticsearch. You can visualize them using Kibana (if configured).

## Running Chaos Tests

To test the resilience of the system, you can use the provided chaos test script:
    ```
    chmod +x chaos_test.sh
    ./chaos_test.sh
    ```

This script will randomly kill services to simulate failures.

## Health Checks and Testing

This project includes scripts for health checking and running tests:

1. `health_check.sh`: This script checks the health of the services and their interactions.

   To run the health check:
   ```
   chmod +x health_check.sh
   ./health_check.sh
   ```

   This script will:
   - Check if the user and order services are responding
   - Test the interaction between services by creating an order
   - Restart services if they're not responding

2. `run_tests.sh`: This script combines chaos testing with health checks.

   To run the tests:
   ```
   chmod +x run_tests.sh
   ./run_tests.sh
   ```

   This script will:
   - Start the chaos test in the background
   - Continuously run health checks while the chaos test is running
   - Perform a final health check after the chaos test completes

These scripts help ensure the resilience of your microservices architecture by simulating failures and verifying the system's ability to recover.

## Project Structure

- `services/`: Contains the User and Order microservices
- `dashboard/`: Web dashboard for monitoring service health
- `prometheus/`: Prometheus configuration
- `fluentd/`: Fluentd configuration for log aggregation
- `chaos_test.sh`: Script for chaos testing

## Configuration

- Prometheus configuration: `prometheus/prometheus.yml`
- Fluentd configuration: `fluentd/conf/fluent.conf`

## Development

To run services locally for development:

1. Install dependencies:
   ```
   pip install -r services/user_service/requirements.txt
   pip install -r services/order_service/requirements.txt
   pip install -r dashboard/requirements.txt
   ```

2. Run each service in a separate terminal:
   ```
   python services/user_service/app.py
   python services/order_service/app.py
   python dashboard/app.py
   ```

## Conclusion

This Resilient Microservices Demo project showcases various aspects of building and maintaining a robust, fault-tolerant microservices architecture. By implementing features such as circuit breakers, retry mechanisms, and chaos testing, it demonstrates how to create a system that can withstand and recover from failures.

Feel free to explore the code, run the tests, and experiment with the system to gain hands-on experience with these concepts.

Thank you for your interest in this project. If you have any questions or feedback, please don't hesitate to open an issue or reach out to me.