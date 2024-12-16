#!/bin/bash
exec gunicorn --bind "0.0.0.0:$PORT" myproject.wsgi:application