from flask import Flask, jsonify, request, abort, make_response, Response
from flask_restful import Resource, Api
from structs.UserInfoData import UserInfoData
import app_var
from flask_jwt_extended import jwt_required
from utils.mongoUtils import update_document
from werkzeug.security import generate_password_hash, check_password_hash
from dateutil import parser
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

import json
from utils.returnJSON import returnJSON


class UserInfo(Resource):
    @jwt_required
    def get(self, username):
        print("YOU ARE " + get_jwt_identity())
        try:
            # Verify user is friend (TODO friend)
            d = UserInfoData.objects.get(username=username)

            return returnJSON(d)
        except Exception as e:
            app_var.app.logger.info(str(e))
            abort(403)

    def delete(self, username):
        return "TODO"


class MyUserInfo(Resource):
    @jwt_required
    def get(self):
        pass
        try:
            d = UserInfoData.objects.get(username=get_jwt_identity())
            return returnJSON(d)
        except Exception as e:
            app_var.app.logger.info(str(e))
            abort(403)


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
            json_data["username"]
        except:
            return "Username field not found", 403
        try:
            d = UserInfoData.objects.get(username=json_data["username"])
            return "User already exist", 403
        except:
            update_document(newUser, json_data)
            newUser.password = generate_password_hash(json_data["password"])
            newUser.birthday = parser.parse(json_data["birthday"])

            try:
                newUser.save()
            except:
                return "User already exist or another error", 403

            app_var.app.logger.info("New user: " + json_data["username"])
        return returnJSON(d)
