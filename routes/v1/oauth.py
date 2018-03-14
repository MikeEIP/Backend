from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask import Flask, request, jsonify
from flask_restful import Resource
from structs.UserInfoData import UserInfoData
from werkzeug.security import generate_password_hash, check_password_hash


class OauthRoute(Resource):
    def post(self):
        if not request.is_json:
            return "Missing JSON in request", 400
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        if not username:
            return "Missing username parameter", 400
        if not password:
            return "Missing password parameter", 400
        try:
            d = UserInfoData.objects.get(pseudo=username)

            if check_password_hash(d.password, password) is False:
                return "bad password", 401
            access_token = create_access_token(identity=username, expires_delta=False)
            return {'access_token': access_token}, 200
        except Exception as e:
            return "Bad username or password", 401
