import os

DEBUG = bool(int(os.environ.get('DEBUG', 0)))

HOST = os.environ.get('HOST', '127.0.0.1')
PORT = os.environ.get('PORT', '5000')