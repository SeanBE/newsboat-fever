import os

host = os.getenv("FEVER_HOST", "0.0.0.0")
port = os.getenv("FEVER_PORT", "5000")

wsgi_app = "api:app"
bind = f"{host}:{port}"
loglevel = os.getenv("FEVER_LOG_LEVEL", "INFO")
workers = 1  # whilst we use the newsboat lockfile approach
