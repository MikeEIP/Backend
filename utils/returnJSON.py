from flask import Response


def returnJSON(obj):
    resp = Response(response=obj.to_json(), status=200, mimetype="application/json")
    resp.headers["Content-Type"] = "text/json; charset=utf-8"
    return resp
