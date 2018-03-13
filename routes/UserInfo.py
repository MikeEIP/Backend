from flask import Flask
from flask_restful import Resource, Api
import utils.mongoConnect as mg
import structs.UserInfoData


class UserInfo(Resource):
    def get(self, pseudo):
        d = structs.UserInfoData.UserInfoData.objects(pseudo=pseudo)
        if d.count() <= 0:
            return "User not found", 404
        return d.to_json()

