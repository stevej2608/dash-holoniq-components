from sys import argv
from utils import logging, log
from examples.form.index import form_example

try:
    index = argv.index('--port')
    port = argv[index+1]
except Exception:
    port = '5050'

print(f' * Visit http://default:{port}')


if __name__ == '__main__':

    # Turn off werkzeug logging as it's very noisy

    aps_log = logging.getLogger('werkzeug')
    aps_log.setLevel(logging.ERROR)

    form_example(port)
