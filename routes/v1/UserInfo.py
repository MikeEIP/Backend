from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import utils.mongoConnect as mg
from structs.UserInfoData import UserInfoData


class UserInfo(Resource):
    def get(self, pseudo):
        d = UserInfoData.objects(pseudo=pseudo)
        if d.count() <= 0:
            return "User not found", 404
        return d.to_json()

    def post(self, pseudo):
        json_data = request.get_json(force=True)
        newUser = UserInfoData()
        # newUser.nom =
        return "TODO"
