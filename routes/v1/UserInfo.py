from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from structs.UserInfoData import UserInfoData
import app_var
from flask_jwt import jwt_required


class UserInfo(Resource):
    @jwt_required()
    def get(self, pseudo):
        try:
            d = UserInfoData.objects.get(pseudo=pseudo)
            return d.to_json()
        except Exception as e:
            return "User not found", 404

    def post(self, pseudo):
        json_data = request.get_json(force=True)
        newUser = UserInfoData()
        # newUser.nom =
        return "TODO"
