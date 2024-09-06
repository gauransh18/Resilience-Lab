#!/bin/bash

CONTAINER_NAME="resiliencelab-user_service-1"

# Function to check if the user service is running
check_service() {
  if curl -s "http://localhost:5001/users" > /dev/null; then
    echo "User service is responding."
    return 0
  else
    echo "User service is not responding."
    return 1
  fi
}

# Function to recover the service
recover_service() {
  echo "Attempting to recover user service..."
  
  # Stop the container if it exists
  if docker ps -a -q -f name=$CONTAINER_NAME | grep -q .; then
    echo "Stopping existing container..."
    docker stop $CONTAINER_NAME
  fi

  # Remove the container if it exists
  if docker ps -a -q -f name=$CONTAINER_NAME | grep -q .; then
    echo "Removing existing container..."
    docker rm $CONTAINER_NAME
  fi

  # Start a new container
  echo "Starting new container..."
  docker-compose up -d user_service
  
  echo "Waiting for the container to start..."
  sleep 10  # Give the container some time to start up
}

# Check if the user service container is running
if docker ps -f name=$CONTAINER_NAME | grep -q $CONTAINER_NAME; then
  echo "User service container is running."
  if ! check_service; then
    echo "User service is not responding, attempting recovery..."
    recover_service
  fi
else
  echo "User service container is down, attempting recovery..."
  recover_service
fi

# Final check after attempting to recover
if docker ps -f name=$CONTAINER_NAME | grep -q $CONTAINER_NAME; then
  echo "User service container is running."
  if ! check_service; then
    echo "User service is still not responding, checking logs..."
    docker logs $CONTAINER_NAME
  fi
else
  echo "Failed to recover user service container. Checking logs..."
  docker logs $CONTAINER_NAME 2>/dev/null || echo "No logs available. Container might not exist."
fi