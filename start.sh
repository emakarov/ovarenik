#!/bin/bash
# run this as the djangorunner user!

VIRTUALENV_DIR=/home/makarov/envs/ovarenik
source $VIRTUALENV_DIR/bin/activate
cd /home/makarov/ovarenik/
python manage.py runfcgi method=threaded debug=False host=127.0.0.1 port=8099 pidfile=/home/makarov/runfiles/ovarenik.pid
