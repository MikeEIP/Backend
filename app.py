import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = 'true'
os.environ['DEBUG'] = 'true'

import sys
from flask import Flask
from flask_restful import Api
from utils.getConfig import Config
import logging
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import utils.mongoConnect

# Var
import app_var

app_var.app = Flask(__name__)
c = Config("config.json")
app_var.app.config['SECRET_KEY'] = c.getField("security", "secret-key")

# Oauth
import routes.v1.oauth

app_var.oauth = JWTManager(app_var.app)

# Api Restfull
app_var.api = Api(app_var.app)

# Import routes
from utils.RouteFactory import getRouteFactory
import routes.v1.UserInfo

APP_VERSION = "v1"


def loggingInit(app: Flask):
    file_handler = logging.FileHandler('app.log')
    stream_handler = logging.StreamHandler(sys.stdout)

    app.logger.addHandler(file_handler)
    app.logger.addHandler(stream_handler)

    app.logger.setLevel(logging.INFO)


def initMongo():
    pass  # TODO


def registerRoutes():
    getRouteFactory().register(routes.v1.UserInfo.UserInfo, "/user/<string:pseudo>")
    getRouteFactory().register(routes.v1.UserInfo.GeneralUserInfo, "/user")
    getRouteFactory().register(routes.v1.oauth.OauthRoute, "/login")


if __name__ == '__main__':
    c = Config("config.json")
    initMongo()
    loggingInit(app_var.app)
    getRouteFactory().giveApp(app_var.app, app_var.api, APP_VERSION)

    registerRoutes()

    app_var.app.run(debug=True, host=c.getField("server", "url"), port=c.getFieldAs("int", "server", "port"))
