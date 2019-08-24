from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings.configs import DATABASE
from contextlib import contextmanager
from log import create_logger

db_logger = create_logger("db")

Base = declarative_base()

engine = None

DB_STRING = {
    "mysql": "mysql://{account}:{password}@{host}:{port}/{db_name}?charset=utf8mb4",
    "postgre": "postgresql://{account}:{password}@{host}:{port}/{db_name}"
}

try:
    DB = DATABASE['database']
    if DB is not None:
        engine = create_engine(DB_STRING[DB].format(
            account=DATABASE['account'],
            password=DATABASE['password'],
            host=DATABASE['host'],
            port=DATABASE['port'],
            db_name=DATABASE['db_name'],
        ))
    else:
        print('데이터베이스 설정이 필요합니다.')
        db_logger.warning("데이터베이스 설정이 필요합니다.")
except KeyError as key:
    print('데이터베이스 설정이 필요합니다. {}'.format(key))
    db_logger.warning("데이터베이스 설정이 필요합니다.{}".format(key))

if engine is not None:
    Session = sessionmaker(bind=engine)

    @contextmanager
    def session_scope(session=None):
        if session:
            yield session
        else:
            session = Session()
        try:
            yield session
            session.commit()
            session.flush()
        except Exception as e:
            session.rollback()
            print('[error] faild db commit')
            print(e)
            db_logger.warning("failed session")
            db_logger.warning(e)
            raise
        finally:
            session.close()
else:
    db_logger.warning("failed connect")
    print('데이터베이스 연결 실패')


def migrate():
    from api_v1.account import models
    from api_v1.answer_post import models
    from api_v1.problem_post import models

    print('migrate')
    try:
        Base.metadata.create_all(engine)
    except BaseException as e:
        db_logger.warning("migrate waring")
        db_logger.warning(e)

