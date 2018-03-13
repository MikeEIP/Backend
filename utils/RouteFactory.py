from flask import Flask
from flask_restful import Resource, Api
from utils.Singleton import SingletonType


class RouteFactory(object, metaclass=SingletonType):
    __instance = None  # type: None or RouteFactory

    @staticmethod
    def _get() -> 'RouteFactory':
        """ Static access method. """
        if RouteFactory.__instance is None:
            RouteFactory()
        return RouteFactory.__instance

    def register(self, cl: Resource, path: str, *optionnalPath):
        path = "/" + self.version + path

        if path in self.routes:
            raise Exception("Route Already exist " + path)  # Replace by log

        for opt in optionnalPath:
            opt = "/" + self.version + opt
            if opt in self.routes or opt == path:
                raise Exception("Route Already exist " + opt)  # Replace by log

        for opt in optionnalPath:
            opt = "/" + self.version + opt
            self.routes[opt] = cl

        else:
            tmp = ""
            for opt in optionnalPath:
                tmp = " /" + self.version + opt

            self.app.logger.info("Adding route " + path + tmp)
            self.routes[path] = cl
            self.api.add_resource(cl, path, *optionnalPath)

    def giveApp(self, app: Flask, api: Api, version: str):
        self.app = app
        self.api = api
        self.version = version

    def __init__(self):
        self.routes = dict()
        self.app = None  # type: Flask
        self.api = None  # type: Api
        self.version = "v1"  # type: str

        """ Virtually private constructor. """
        if RouteFactory.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            RouteFactory.__instance = self


def getRouteFactory() -> RouteFactory:
    return RouteFactory._get()
