#!/bin/bash

timestamp=$(date +"%d-%m_%H-%M")
#ros2 launch stretch_nav2 navigation.launch.py map:=/home/hello-robot/stretch_user/maps/howie_m_final_modified.yaml > /home/hello-robot/bad_nav2/navigation_$timestamp.txt 2>&1 &
/home/hello-robot/smarthome_ws/src/smart-home-robot/helper_scripts/nav2_failure_monitor.sh > /home/hello-robot/nav2_monitor_logs/nav2_monitor_$timestamp.txt  2>&1 &

sleep 25s

ros2 service call /runstop std_srvs/srv/SetBool data:\ false\ &

ros2 launch yaml_tf_broadcaster tf_broadcast_helper.launch.py &
ros2 launch shr_plan action_servers.launch.py > /tmp/action_server.txt 2>&1 &

sleep 10s

