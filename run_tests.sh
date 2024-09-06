#!/bin/bash

#run in bg
./chaos_test.sh &
chaos_pid=$!

# check health_check.sh repeatedly until chaos_test.sh is done
while kill -0 $chaos_pid 2>/dev/null; do
    ./health_check.sh
    sleep 45 
done

wait $chaos_pid

./health_check.sh

echo "tests completed"