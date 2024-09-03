#!/bin/bash

if ! curl -s http://localhost:5000/users; then
    echo "User service is down, restarting..."
    docker restart user_service
fi