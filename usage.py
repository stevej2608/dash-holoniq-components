from sys import argv
from utils import logging, log
from examples.form.index import create_app
from app import serve_app

try:
    index = argv.index('--port')
    port = argv[index+1]
except Exception:
    port = '5050'

print(f' * Visit http://default:{port}')


if __name__ == '__main__':
    app = create_app()
    serve_app(app)
