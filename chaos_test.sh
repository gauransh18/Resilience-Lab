#!/bin/bash

chaos_action() {
    services=("resiliencelab-user_service-1" "resiliencelab-order_service-1" "dummy-service")
    random_service=${services[$RANDOM % ${#services[@]}]}
    
    if [ "$random_service" == "dummy-service" ]; then
        echo "dummy-service took one for the team"
    else
        echo "Killing $random_service"
        docker kill $random_service
    fi
}

for i in {1..5}
do
    echo "Running chaos experiment $i"
    
    chaos_action
    
    echo "Waiting for 1 minute before next experiment..."
    sleep 60
done

echo "Chaos testing completed"