from flask_restful import Resource
from log import create_logger
from flask import request
from flask_restful import reqparse
from api_v1.problem_post.problem_post_service import ProblemPostService
from Utils.utils import set_response


class ProblemPost(Resource):
    logger = create_logger(__name__)

    def get(self):
        return __name__ + "GET"

    def post(self):
        self.logger.info("---> ProblemPost create")
        try:
            params = request.get_json()
            self.logger.info(params)
            if params is None:
                parser = reqparse.RequestParser()
                parser.add_argument('request')
                args = parser.parse_args()
                self.logger.info(args)

                params = vars(args)
                self.logger.info("파라미터")
                self.logger.info(params)


            file = request.files['file']

            self.logger.info(params)
            self.logger.info(file)
            response = ProblemPostService.mysql_create_problem_post(params, file)
            print(file)
        except BaseException as e:
            self.logger.info("problemPost create params error")
            self.logger.info(e)
            response = set_response("88", {"errorMsg": "문제를 생성중 에러가 발생했습니다."})

        return response

    def put(self):
        return __name__ + "Put"
