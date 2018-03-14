from flask import Flask, jsonify, request, abort, make_response, Response
from flask_restful import Resource, Api
from structs.UserInfoData import UserInfoData
import app_var
from flask_jwt_extended import jwt_required
from utils.mongoUtils import update_document
from werkzeug.security import generate_password_hash, check_password_hash
from dateutil import parser
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

import json
from utils.returnJSON import returnJSON


class UserInfo(Resource):
    @jwt_required
    def get(self, pseudo):
        print("YOU ARE " + get_jwt_identity())
        try:
            # Verify user is friend (TODO friend)
            d = UserInfoData.objects.get(pseudo=pseudo)

            return returnJSON(d)
        except Exception as e:
            print(str(e))
            abort(403)

    def post(self, pseudo):
        return jsonify(salut="BONJOUR")
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
        """
        Signup a user
        """
        json_data = ""

        try:
            json_data = request.get_json(force=True)
        except:
            return "Failed to parse json", 403

        newUser = UserInfoData()

        try:
            json_data["pseudo"]
        except:
            return "Pseudo field not found", 403
        try:
            d = UserInfoData.objects.get(pseudo=json_data["pseudo"])
            return "User already exist", 403
        except:
            update_document(newUser, json_data)
            newUser.password = generate_password_hash(json_data["password"])
            newUser.birthday = parser.parse(json_data["birthday"])
            newUser.save()

            app_var.app.logger.info("New user: " + json_data["pseudo"])
        return returnJSON(d)
