from api_v1.account.models import Customer
from settings.database import session_scope
from api_v1.account.Utils import AccountUtils
from log import create_logger
from Utils.utils import set_response


class CusAuthService:
    logger = create_logger(__name__)

    @classmethod
    def IsUseAccount(cls, email):
        with session_scope() as session:
            isUse = session.query(Customer).filter(Customer.email == email).first()
        if isUse is None:
            return False
        return True

    @classmethod
    def create_user(cls, email, pwd):
        cls.logger.info("create_user")
        cls.logger.info(email)
        cls.logger.info(pwd)

        cus = None
        try:
            salt = AccountUtils.getn_salt()
            hashed_pwd = AccountUtils.set_pwd(pwd, salt)
            cid = AccountUtils.get_timestamp('CUS')

            with session_scope() as session:
                customer = Customer()
                customer.cid = cid
                customer.salt = salt
                customer.email = email
                customer.password = hashed_pwd
                session.add(customer)
                cus = {
                    'email': email,
                    'uid': cid
                }
        except BaseException as e:
            cls.logger.warning("유저 생성중 문제가 발생했습니다.")
            cls.logger.warning(e)
            return set_response("99", {"errorMsg": "유저 생성중 문제가 발생했습니다."})

        try:
            access_token = AccountUtils.get_token(cus)
        except BaseException as e:
            cls.logger.warning("토큰 생성중 에러가 발생했습니다.")
            cls.logger.warning(e)
            return set_response("99", {"errorMsg": "토큰 생성중 에러가 발생했습니다."})
        return set_response("00", {'token': access_token})

    @classmethod
    def login(cls, email, pwd):
        # 아이디, pwd 확인
        cls.logger.info("login 진입")
        with session_scope() as session:
            customer = session.query(Customer).filter(Customer.email == email).first()
            cls.logger.info("{} 조회성공".format(customer.email))

            if customer is None:
                response = set_response("99", {"errorMsg": "존재하지 않는 이메일입니다."})
                return response
            try:
                cid = customer.cid
                cus_pwd = customer.password
                salt = customer.salt
                pwd = AccountUtils.set_pwd(pwd, salt)
                isauth = AccountUtils.chk_pwd(pwd, cus_pwd)
                if isauth:
                    cus = {
                        'email': email,
                        'uid': cid
                    }
                    access_token = AccountUtils.get_token(cus)
                    response = set_response("00", {"token": access_token})
            except BaseException as e:
                cls.logger.warning("크리티컬 이슈")
                cls.logger.warning(e)
                response = set_response("99", {"errorMsg": '토큰 생성 실패'})
            else:
                response = set_response("99", {"errorMsg": '회원정보가 틀렸습니다.'})
        return response
