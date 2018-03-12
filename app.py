import sys
from flask import Flask
from utils.RouteFactory import RouteFactory as rf
import logging

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


def loggingInit(app: Flask):
    file_handler = logging.FileHandler('app.log')
    stream_handler = logging.StreamHandler(sys.stdout)

    app.logger.addHandler(file_handler)
    app.logger.addHandler(stream_handler)

    app.logger.setLevel(logging.INFO)


if __name__ == '__main__':
    loggingInit(app)
    rf.get()

    app.run(debug=True)
