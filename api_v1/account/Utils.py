from flask import request, jsonify, g
from settings.configs import config
from functools import wraps
from datetime import datetime as dt
import bcrypt
import jwt
from log import create_logger


class AccountUtils:
    logger = create_logger(__name__)

    @classmethod
    def set_pwd(cls, pwd, salt):
        try:
            cls.logger.info(pwd)
            cls.logger.info(type(pwd))
            pwd = pwd.encode()
            hash_pwd = bcrypt.hashpw(pwd, salt.encode()).hex()
        except BaseException as e:
            cls.logger.warning('비밀번호 생성 오류')
            cls.logger.warning(e)
            raise
        return hash_pwd

    @classmethod
    def chk_pwd(cls, pwd, hash_pwd):
        pwd = pwd.encode()
        hash_pwd = hash_pwd.encode()
        if pwd == hash_pwd:
            return True
        else:
            return False
        # return bcrypt.checkpw(pwd, hash_pwd)

    @classmethod
    def create_token(cls, payload):
        access_token = jwt.encode(payload, config['SECRET_KEY'], algorithm='HS256')
        return access_token.decode()

    @classmethod
    def get_timestamp(cls, prefix):
        timestamp = int(dt.now().timestamp()*1000000)
        stamp = "{}{}".format(prefix, timestamp)
        return stamp

    @classmethod
    def get_token(cls, payload):
        access_token= cls.create_token(payload)
        return access_token

    @classmethod
    def getn_salt(cls):
        return bcrypt.gensalt()