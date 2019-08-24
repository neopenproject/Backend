import importlib
import sys
import jwt

from flask import Flask, request, abort, g
from flask_restful import Api
from settings import configs, database
from log import create_logger

main_logger = create_logger(__name__)

app = Flask(__name__)
app.config.from_object(configs.config)

api = Api(app)

urls = importlib.import_module(configs.ROOT_URL)

for res, url in urls.urlpatterns:
    if urls.prefix_url is not None:
        url = urls.prefix_url + url
    api.add_resource(res, url)


@app.errorhandler(401)
def auth_faild(error):
    return '인증실패', 401


@app.before_request
def before_request():
    access_token = request.headers.get("Authorization")
    if access_token is not None:
        try:
            # if not isinstance(access_token, str):
            #     access_token = access_token.encode()
            payload = jwt.decode(access_token, configs.config['SECRET_KEY'])
        except BaseException as e:
            main_logger.warning(e)
            main_logger.warning("access error")
            return abort(401)
        if payload is not None:
            uid = payload['uid']
            email = payload['email']
            main_logger.info(uid)
            g.uid = uid
            g.user_email = email


def run():
    if __name__ == "__main__":
        app.run('localhost', 1472)


command_task = {
    'migrate': database.migrate,
    'run': run
}

for command in sys.argv[1:]:
    try:
        command_task[command]()
    except KeyError as key:
        print("{} key error".format(key))







