#!/bin/bash

CONTAINER_NAME="resiliencelab-user_service-1"

check_service() {
  service_name=$1
  port=$2
  response=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:$port)
  if [ $response -eq 200 ]; then
    echo "$service_name is healthy"
  else
    echo "$service_name is not responding, restarting..."
    docker-compose restart $service_name
  fi
}

# checking services
check_service "user_service" 5001
check_service "order_service" 5002

# checking interconnection between user and order service
create_order_response=$(curl -s -o /dev/null -w "%{http_code}" -X POST -H "Content-Type: application/json" -d '{"user_id": 1, "product": "Test Product"}' http://localhost:5002/create_order)
if [ $create_order_response -eq 201 ]; then
    echo "Services interaction is healthy"
else
    echo "Services interaction failed, check logs for more details or may be no more try :)"
fi