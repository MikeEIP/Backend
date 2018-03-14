from flask import Flask, jsonify, request, abort
from flask_restful import Resource, Api
from structs.UserInfoData import UserInfoData
import app_var
from flask_jwt_extended import jwt_required
from utils.mongoUtils import update_document
from werkzeug.security import generate_password_hash, check_password_hash
from dateutil import parser


class UserInfo(Resource):
    @jwt_required
    def get(self, pseudo):
        try:
            # Verify user is himself OR friend (TODO friend)
            d = UserInfoData.objects.get(pseudo=pseudo)
            return d.to_json()
        except Exception as e:
            abort(403)

    def post(self, pseudo):
        # json_data = request.get_json(force=True)
        # newUser = UserInfoData()
        # newUser.nom =
        return "TODO"


class GeneralUserInfo(Resource):
    @jwt_required
    def get(self):
        # TODO
        abort(403)

    def post(self):
        json_data = request.get_json(force=True)
        newUser = UserInfoData()

        try:
            json_data["pseudo"]
        except:
            return "Failed to parse json", 403
        try:
            d = UserInfoData.objects.get(pseudo=json_data["pseudo"])
            return "User already exist", 403
        except:
            update_document(newUser, json_data)
            newUser.password = generate_password_hash(json_data["password"])
            newUser.birthday = parser.parse(json_data["birthday"])
            newUser.save()

            app_var.app.logger.info("New user: " + json_data["pseudo"])
        return newUser.to_json()
