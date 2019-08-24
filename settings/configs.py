import os

# LOCAL, TEST, REAL
MODE = 'LOCAL'

ROOT_URL = 'api_v1.urls'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# [시간][모듈명][파일명 - 호출] 내용
FORMAT_STRING = '[%(levelname)s][%(asctime)s][%(name)s][line : %(lineno)s][func : %(funcName)2s()] %(message)s'

config = {
    'SECRET_KEY': 'neok4ng49m*kt258g)%)ss%h-^w+l7b+#lvmhu(c0d!ik5!%+26i!olas'
}

DATABASE = {
    'database': 'mysql',
    'account': 'nepenthes',
    'password': 'win3758e',
    'db_name': 'test',
    'host': 'mysql-nepenthes.ccdd77mi4olw.ap-northeast-2.rds.amazonaws.com',
    'port': '3306'
}
