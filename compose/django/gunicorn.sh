#!/bin/sh
python /app/manage.py collectstatic --noinput
python /app/manage.py compilemessages
/usr/local/bin/gunicorn config.wsgi -w 4 -b 0.0.0.0:5001 --chdir=/app
