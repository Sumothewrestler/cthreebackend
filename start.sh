#!/bin/bash
export PORT=8000
exec gunicorn --config gunicorn.conf.py myproject.wsgi:application 