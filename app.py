import sys
from flask import Flask
from flask_restful import Api
from utils.RouteFactory import getRouteFactory
from utils.getConfig import Config
import logging

# Import routes
import routes.v1.UserInfo

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
    pass


if __name__ == '__main__':
    c = Config("config.json")
    initMongo()
    loggingInit(app)
    getRouteFactory().giveApp(app, api, APP_VERSION)
    getRouteFactory().register(routes.v1.UserInfo.UserInfo, "/user/<string:pseudo>")

    app.run(debug=True, host=c.getField("server", "url"), port=c.getFieldAs("int", "server", "port"))
