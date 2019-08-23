import os

# LOCAL, TEST, REAL
MODE = 'LOCAL'

ROOT_URL = 'api_v1.urls'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# [시간][모듈명][파일명 - 호출] 내용
FORMAT_STRING = '[%(levelname)s][%(asctime)s][%(name)s][line : %(lineno)s][func : %(funcName)2s()] %(message)s'

config = {
    'SECRET_KEY': 'ABCDEFGASD'
}

DATABASE = {
    'database': 'mysql',
    'account': 'root',
    'password': 'test123',
    'db_name': 'test',
    'host': 'localhost',
    'port': '3306'
}