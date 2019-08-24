from flask_restful import Resource, reqparse
from flask import request, g, abort
from log import create_logger
from Utils.utils import set_response
from api_v1.answer_post.answer_post_service import AnswerPostService


class AnswerPost(Resource):
    logger = create_logger(__name__)

    def get(self):
        try:
            filters = request.args

            count, answer_post = AnswerPostService.mysql_fetch_answer_post(filters)
            response = set_response("00", {"answer_post": answer_post, "count": count})
        except BaseException as e:
            self.logger.warning("answer get error")
            self.logger.warning(e)
            response = set_response("77", {"errorMsg": "답안 요청중 에러가 발생했습니다."})
        return response

    def post(self):
        self.logger.info("---> ProblemPost create")
        author = g.uid
        if author is None:
            return abort(401)

        try:
            params = request.get_json()
            self.logger.info(params)
            if params is None:
                parser = reqparse.RequestParser()
                parser.add_argument('time')
                parser.add_argument('is_over')
                parser.add_argument('problem_post')
                args = parser.parse_args()
                self.logger.info(args)
                params = {
                    'time': args.time,
                    'is_over': True if args.is_over == "true" else False,
                    'problem_post': args.problem_post,
                    'author': author
                }
                self.logger.info("파라미터")
                self.logger.info(params)

            file = request.files['file']

            self.logger.info(params)
            self.logger.info(file)
            response = AnswerPostService.mysql_create_answer_post(params, file)
            print(file)
        except BaseException as e:
            self.logger.info("answer create params error")
            self.logger.info(e)
            response = set_response("88", {"errorMsg": "문제를 생성중 에러가 발생했습니다."})

        return response

    def put(self):
        return "Answer Put"
