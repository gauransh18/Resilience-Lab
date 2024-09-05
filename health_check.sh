#!/bin/bash

if ! curl -s http://localhost:5001/users; then
    echo "User service is down, restarting..."
    docker restart user_service
fi