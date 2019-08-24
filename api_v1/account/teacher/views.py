from flask_restful import Resource
from flask import request, jsonify
from Utils.utils import set_response
from log import create_logger
from api_v1.account.teacher.tea_auth_service import TeaAuthService


class TeacherAccount(Resource):
    logger = create_logger(__name__)

    def get(self):
        return jsonify({"code": "00", "results": "asd"})

    def post(self):
        try:
            params = request.get_json()
            email = params['email']
            pwd = params['pwd']

            # 이메일 존재하는지
            if not TeaAuthService.IsUseAccount(email):
                response = TeaAuthService.create_user(email, pwd)  # 존재 하지 않다면 회원가입
            else:
                response = set_response("C01", "이미 존재하는 이메일 입니다.")

        except BaseException as e:
            error_msg = "시스템 에러가 발생했습니다."
            self.logger.warning(error_msg)
            self.logger.warning(e)
            response = set_response("01", error_msg)
        return jsonify(response)

    def put(self):
        pass

    def delete(self):
        pass


class TeaAuthView(Resource):
    logger = create_logger(__name__)

    def get(self):
        pass

    def post(self):
        try:
            params = request.get_json()
            email = params['email']
            pwd = params['pwd']

            # 로그인
            response = TeaAuthService.login(email, pwd)

        except BaseException as e:
            error_msg = "시스템 에러가 발생했습니다."
            self.logger.warning(error_msg)
            self.logger.warning(e)
            response = set_response("01", error_msg)
        return jsonify(response)