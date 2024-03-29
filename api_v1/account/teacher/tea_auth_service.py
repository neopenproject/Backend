from api_v1.account.models import Teacher
from settings.database import session_scope
from api_v1.account.Utils import AccountUtils
from log import create_logger
from Utils.utils import set_response


class TeaAuthService:
    logger = create_logger(__name__)

    @classmethod
    def IsUseAccount(cls, email):
        with session_scope() as session:
            isUse = session.query(Teacher).filter(Teacher.email == email).first()
        if isUse is None:
            return False
        return True

    @classmethod
    def create_user(cls, email, pwd):
        cls.logger.info("create_user Teacher")
        cls.logger.info(email)
        cls.logger.info(pwd)

        cus = None
        try:
            salt = AccountUtils.getn_salt()
            hashed_pwd = AccountUtils.set_pwd(pwd, salt)
            tid = AccountUtils.get_timestamp('TEA')

            with session_scope() as session:
                teacher = Teacher()
                teacher.tid = tid
                teacher.salt = salt
                teacher.email = email
                teacher.password = hashed_pwd
                session.add(teacher)
                tea = {
                    'email': email,
                    'uid': tid
                }
        except BaseException as e:
            cls.logger.warning("유저 생성중 문제가 발생했습니다.")
            cls.logger.warning(e)
            return set_response("99", {"errorMsg": "유저 생성중 문제가 발생했습니다."})

        try:
            access_token = AccountUtils.get_token(tea)
        except BaseException as e:
            cls.logger.warning("토큰 생성중 에러가 발생했습니다.")
            cls.logger.warning(e)
            return set_response("99", {"errorMsg": "토큰 생성중 에러가 발생했습니다."})
        return set_response("00", {'token': access_token})

    @classmethod
    def login(cls, email, pwd):
        # 아이디, pwd 확인
        with session_scope() as session:
            teacher = session.query(Teacher).filter(Teacher.email == email).first()
            if teacher is None:
                response = set_response("99", {"errorMsg": "존재하지 않는 이메일입니다."})
                return response
            tid = teacher.tid
            cus_pwd = teacher.password
            salt = teacher.salt
            pwd = AccountUtils.set_pwd(pwd, salt)
            isauth = AccountUtils.chk_pwd(pwd, cus_pwd)
            if isauth:
                cus = {
                    'email': email,
                    'uid': tid
                }
                access_token = AccountUtils.get_token(cus)
                response = set_response("00", {"token": access_token})
            else:
                response = set_response("99", {"errorMsg": '회원정보가 틀렸습니다.'})
        return response
