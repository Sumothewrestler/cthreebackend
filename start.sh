#!/bin/bash
export PORT=8000
exec gunicorn --bind 0.0.0.0:8000 myproject.wsgi:application