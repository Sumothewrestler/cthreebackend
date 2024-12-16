import os

bind = "0.0.0.0:8000"  # Explicitly set to port 8000
workers = 4
worker_class = 'gthread'
threads = 4
timeout = 120