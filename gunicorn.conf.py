# gunicorn.conf.py
import os

port = int(os.getenv('PORT', 8000))
bind = f'0.0.0.0:{port}'
workers = 4
threads = 4
timeout = 120