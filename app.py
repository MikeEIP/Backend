import sys
from flask import Flask
from flask_restful import Resource, Api
from utils.RouteFactory import getRouteFactory
import logging

# Import routes
import routes.UserInfo

app = Flask(__name__)
api = Api(app)

APP_VERSION = "v1"


def loggingInit(app: Flask):
    file_handler = logging.FileHandler('app.log')
    stream_handler = logging.StreamHandler(sys.stdout)

    app.logger.addHandler(file_handler)
    app.logger.addHandler(stream_handler)

    app.logger.setLevel(logging.INFO)


def initMongo():
    import utils.mongoConnect


if __name__ == '__main__':
    initMongo()
    loggingInit(app)
    getRouteFactory().giveApp(app, api, APP_VERSION)
    getRouteFactory().register("/user/<string:pseudo>", routes.UserInfo.UserInfo)

    app.run(debug=True)
