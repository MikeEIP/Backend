from flask import Flask
from flask_restful import Api
from flask_oauthlib.provider import OAuth2Provider
from flask_jwt import JWT, jwt_required

app = None
api = None
jwt = None
