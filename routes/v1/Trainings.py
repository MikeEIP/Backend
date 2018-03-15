from flask import abort
from flask_restful import Resource

from structs.ExercicesInfoData import ExercicesInfoData
from flask_jwt_extended import jwt_required
from utils.returnJSON import returnJSON


class Tranings(Resource):
    @jwt_required
    def get(self):
        try:
            d = ExercicesInfoData.objects.all()
            return returnJSON(d)
        except Exception:
            abort(403)

    # """
    # def post(self):
    #     json_data = request.get_json(force=True)
    #     newTraining = ExercicesInfoData()
    #
    #     try:
    #         json_data["username"]
    #     except:
    #         return "Failed to parse json", 403
    #     try:
    #         d = UserInfoData.objects.get(pseudo=json_data["username"])
    #         return "User already exist", 403
    #     except:
    #         update_document(newTraining, json_data)
    #         newTraining.save()
    #
    #     return newTraining.to_json()
    # """
