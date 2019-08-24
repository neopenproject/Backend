from flask_restful import Resource
from log import create_logger
from flask import request
from Utils.utils import set_response


class ProblemPost(Resource):
    logger = create_logger(__name__)

    def get(self):
        return __name__ + "GET"

    def post(self):
        return __name__ + "POST"

    def put(self):
        return __name__ + "Put"
