rm -rf ~/deepdungeons/logs/runserver.log

python ~/deepdungeons/manage.py runserver >> ~/deepdungeons/logs/runserver.log 2>&1 &

mkdir -p ~/deepdungeons/logs
touch ~/deepdungeons/logs/runserver.log
echo "Starting server..." >> ~/deepdungeons/logs/runserver.log