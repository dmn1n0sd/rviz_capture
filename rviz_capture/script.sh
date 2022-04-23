#!/bin/bash
#echo "test"
pushd $1
#ros2 run record_starter.py
for file in `ls `; do
    echo "play ${file}"
    ros2 bag play_revised ${file}
done 
popd
