#!/bin/bash

rm -rf ~/deepdungeons/logs/killserver.log

sudo kill $(sudo lsof -t -i:8000)

mkdir -p ~/deepdungeons/logs
touch ~/deepdungeons/logs/killserver.log
echo "Killed server at PID "$(sudo lsof -t -i:8000) >> ~/deepdungeons/logs/killserver.log