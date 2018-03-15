import os
import sys
from flask import Flask
from flask_restful import Api
from utils.getConfig import Config
import logging
from flask_jwt_extended import JWTManager

# Var
import app_var

# Get config
app_var.CONFIG_PATH = "config.json"

if len(sys.argv) > 1:
    app_var.CONFIG_PATH = sys.argv[1]

app_var.app = Flask(__name__)
c = Config(app_var.CONFIG_PATH)
app_var.app.config['SECRET_KEY'] = c.getField("security", "secret-key")
app_var.app.config['PROPAGATE_EXCEPTIONS'] = True  # In no debug mode, exceptions throw internal error du to
# flaskrestful bug

# Mongo
import utils.mongoConnect

# Oauth
import routes.v1.oauth

app_var.oauth = JWTManager(app_var.app)

# Api Restfull
app_var.api = Api(app_var.app)

# Import routes
from utils.RouteFactory import getRouteFactory
import routes.v1.UserInfo
import routes.v1.Trainings

APP_VERSION = "v1"


def loggingInit(app: Flask):
    file_handler = logging.FileHandler('app.log')
    stream_handler = logging.StreamHandler(sys.stdout)

    app.logger.addHandler(file_handler)
    app.logger.addHandler(stream_handler)

    app.logger.setLevel(logging.INFO)


def initMongo():
    utils.mongoConnect.connectToMongo()


def registerRoutes():
    print("\n===== ROUTES =====")
    getRouteFactory().register(routes.v1.UserInfo.UserInfo, "/user/<string:username>")
    getRouteFactory().register(routes.v1.UserInfo.GeneralUserInfo, "/user")
    getRouteFactory().register(routes.v1.oauth.OauthRoute, "/login")
    getRouteFactory().register(routes.v1.Trainings.Tranings, "/trainings")
    getRouteFactory().register(routes.v1.UserInfo.MyUserInfo, "/user/me")
    print("")


def initDebug(config: Config) -> bool:
    isDebug = config.getField("isDebug")
    if isDebug:
        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = 'true'
        os.environ['DEBUG'] = 'true'
    else:
        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = 'false'
        os.environ['DEBUG'] = 'false'
    return isDebug


def getPortAndUrl(config: Config) -> (str, int):
    config_url = config.getField("server", "url")
    config_port = config.getFieldAs("int", "server", "port")

    tmpStr = "{\n\"server\": {\n\"url\": \"0.0.0.0\",\n\"port\": \"5000\"\n}\n}"

    if config_url is None:
        raise RuntimeError("Url not defined, define it in config.json file or specify config as first argument when "
                           "calling the script. "
                           "\nDefine it like this:\n" + tmpStr)

    if config_port is None:
        raise RuntimeError("Port not defined, define it in config.json file or specify config as first argument when "
                           "calling the script. "
                           "\nDefine it like this:\n" + tmpStr)
    return config_url, config_port


if __name__ == '__main__':
    c = Config(app_var.CONFIG_PATH)
    d = initDebug(c)
    initMongo()
    loggingInit(app_var.app)
    getRouteFactory().giveApp(app_var.app, app_var.api, APP_VERSION)

    registerRoutes()

    url, port = getPortAndUrl(c)
    app_var.app.run(debug=d, host=url, port=port)
