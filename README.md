# Flask_container 
 매 프로젝트마다 다시 설정하는게 너무 번거로워서 기본적인 설정 구현.
  
## url_conf
``setting path : project/settings/configs.py``

  configs 모듈 ROOT_URL 변수에 import 해야하는 모듈작성
  
## database
```
SQLAlchemy  1.3.6
setting path : project/settings/configs.py
DB path : project/settings/database.py
```


 sqlalchemy를 사용하여 ORM 환경을 구축했고 데이터베이스 설정은
 configs.py에서 가능합니다.
 
 기본적으로 연결을 지원하는 데이터베이스는 mysql, postgres 두가지이며 다른 데이터베이스를 사용하고 싶을 경우 database.py에서 DB_STRING을 추가하세요.
 
 [접속지원 데이터베이스]
 ```
    mysql   : mysqlclient==1.4.4
    postgre : psycopg2==2.8.3
 ```
 
## loging
```
path : project/log.py
format path : project/settings/configs.py
```
 로거는 python 기본 logging 모듈을 사용하여 구현했습니다.
 
 log 모듈을 import 하여 create_logger(모듈명)을 통해 로거를 생성하고 사용하세요.  

 로그 문자열 포맷은 configs.py 에서 수정할 수 있습니다.

## command
    python manage.py run // 시작
    python manage.py migrate // DB 테이블 동기화
## 
created_by cslee 2019.08.15
    