from flask_restful import Resource
from flask import request
from Utils.utils import set_response


class AnswerPost(Resource):
    def get(self):
        return "Answer get"

    def post(self):
        # params = request.get_json()
        # files = request.files()
        # if params is None or files is None:
        #     response = set_response("88", {"errorMsg": "필수 값들을 함께 보내주세요."})
        #     return response

        return "Answer Post "

    def put(self):
        return "Answer Put"
