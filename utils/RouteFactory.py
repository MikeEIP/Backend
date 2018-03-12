from flask import Flask
from flask_restful import Resource, Api
from utils.Singleton import SingletonType


class RouteFactory(object, metaclass=SingletonType):
    __instance = None  # type: None or RouteFactory

    @staticmethod
    def get() -> 'RouteFactory':
        """ Static access method. """
        if RouteFactory.__instance is None:
            RouteFactory()
        return RouteFactory.__instance

    def register(self, name: str, cl: Resource):
        if name in self.routes:
            raise Exception("Route Already exist " + name)
        else:

            self.routes[name] = cl
            self.api.add_resource(cl, name)

    def giveApp(self, app: Flask, api: Api):
        self.app = app
        self.api = api

    def __init__(self):
        self.routes = dict()
        self.app = None  # type: Flask
        self.api = None  # type: Api
        """ Virtually private constructor. """
        if RouteFactory.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            RouteFactory.__instance = self
