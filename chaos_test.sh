#!/bin/bash

# Randomly kill the user_service container
container_name="resiliencelab-user_service-1"

# Check if the container is running
if [ "$(docker ps -q -f name=$container_name)" ]; then
    echo "Killing container: $container_name"
    docker kill $container_name
else
    echo "Container $container_name is not running"
fi