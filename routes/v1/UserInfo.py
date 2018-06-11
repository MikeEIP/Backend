from flask import request, abort
from flask_restful import Resource
from structs.UserInfoData import UserInfoData
import app_var
from utils.mongoUtils import update_document
from werkzeug.security import generate_password_hash
from dateutil import parser
from flask_jwt_extended import jwt_required, get_jwt_identity

from utils.returnJSON import returnJSON
from structs.AdminData import AdminInfoData


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
        app_var.app.logger.info("User " + username + " to delete")
        return "TODO"


class MyUserInfo(Resource):
    @jwt_required
    def get(self):
        try:
            d = UserInfoData.objects.get(username=get_jwt_identity())
            return returnJSON(d)
        except Exception as e:
            app_var.app.logger.info(str(e))
            abort(403)

    @jwt_required
    def delete(self):
        app_var.app.logger.info("User " + get_jwt_identity() + " try to delete himself")
        return "TODO"


class GeneralUserInfo(Resource):
    @jwt_required
    def get(self):
        try:
            AdminInfoData.objects.get(username=get_jwt_identity())
            return returnJSON(UserInfoData.objects.all())
        except Exception:
            abort(403)

    def post(self):
        """
        Signup a user
        """
        json_data = ""

        try:
            json_data = request.get_json(force=True)
        except Exception:
            return "Failed to parse json", 403

        newUser = UserInfoData()

        try:
            json_data["username"]
        except Exception:
            return "Username field not found", 403
        try:
            UserInfoData.objects.get(username=json_data["username"])
            return "User already exist", 403
        except Exception:
            try:
                update_document(newUser, json_data)
            except Exception as e:
                app_var.app.logger.info("update document failed " + str(e))
                return "Not enough field or bad field provided", 400
            if len(json.data["password"]) < 8:
                return "bad length", 402
            newUser.password = generate_password_hash(json_data["password"])
            newUser.birthday = parser.parse(json_data["birthday"])

            try:
                newUser.save()
            except Exception as e:
                app_var.app.logger.warning(str(e))
                return "User already exist or another error", 403

            app_var.app.logger.info("New user: " + json_data["username"])
        return returnJSON(newUser)
