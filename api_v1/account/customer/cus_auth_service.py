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
        cus = None
        try:
            salt = AccountUtils.getn_salt()
            hashed_pwd = AccountUtils.set_pwd(pwd, salt)
            cid = AccountUtils.get_timestamp('cus')

            with session_scope() as session:
                customer = Customer()
                customer.cid = cid
                customer.salt = salt
                customer.email = email
                customer.password = hashed_pwd
                session.add(customer)
                cus = {
                    'email': email,
                    'cid': cid
                }
        except BaseException as e:
            cls.logger.warning("유저 생성중 문제가 발생했습니다.")
            cls.logger.warning(e)
            return set_response("99", {"errorMsg": "유저 생성중 문제가 발생했습니다."})

        try:
            access_token = cls.get_token(cus)
        except BaseException as e:
            cls.logger.warning("토큰 생성중 에러가 발생했습니다.")
            cls.logger.warning(e)
            return set_response("99", {"errorMsg": "토큰 생성중 에러가 발생했습니다."})
        return set_response("00", {'token': access_token})

    @classmethod
    def get_token(cls, cus):
        payload = {
            'email': cus.get('email'),
            'cus_id': cus.get('cid'),
        }
        access_token = AccountUtils.create_token(payload)
        return access_token

    @classmethod
    def login(cls, email, pwd):
        # 아이디, pwd 확인
        with session_scope() as session:
            customer = session.query(Customer).filter(Customer.email == email).first()

            if customer is None:
                response = set_response("99", {"errorMsg": "이메일이 틀렸습니다."})
                return response
            cid = customer.cid
            cus_pwd = customer.password
            salt = customer.salt
            pwd = AccountUtils.set_pwd(pwd, salt)
            isauth = AccountUtils.chk_pwd(pwd, cus_pwd)
            if isauth:
                cus = {
                    'email': email,
                    'cid': cid
                }
                access_token = AccountUtils.get_token(cus)
                response = set_response("00", {"token": access_token})
            else:
                response = set_response("99", {"errorMsg": '비밀번호가 틀렸습니다.'})
        return response
