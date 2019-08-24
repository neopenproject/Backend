from flask_restful import Resource
from flask import jsonify

class ApiV1Index(Resource):
    def get(self):
        result = {
            "result" : "pong"
        }
        return jsonify(code="00", result=result)