from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask import Flask, request, jsonify
from flask_restful import Resource
from structs.UserInfoData import UserInfoData
from werkzeug.security import generate_password_hash, check_password_hash
import app_var


class OauthRoute(Resource):
    def post(self):
        if not request.is_json:
            app_var.app.logger.info("User tried to connect but not provide json")
            return "Missing JSON in request", 400
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        if not username:
            app_var.app.logger.info("User tried to connect but not provide username")
            return "Missing username parameter", 400
        if not password:
            app_var.app.logger.info("User tried to connect but not provide password")
            return "Missing password parameter", 400
        try:
            d = UserInfoData.objects.get(username=username)

            if check_password_hash(d.password, password) is False:
                app_var.app.logger.info("User tried to connect but provide bad password, username was " + username +
                                        " password was " + password)
                return "bad password", 401
            access_token = create_access_token(identity=username, expires_delta=False)
            return {'access_token': access_token}, 200
        except Exception as e:
            app_var.app.logger.info("User tried to connect but exception: " + str(e))
            return "Bad username or password", 401
