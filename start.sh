#!/usr/bin/env bash



source /var/www/app/venv/bin/activate
python /var/www/app/manage.py db_init
deactivate

/usr/bin/supervisord