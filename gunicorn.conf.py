# gunicorn.conf.py
import os

port = int(os.getenv('PORT', '8000'))  # Make sure PORT is a string
bind = f'0.0.0.0:{port}'
workers = 4
worker_class = 'gthread'
threads = 4
timeout = 120