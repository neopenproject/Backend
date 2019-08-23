import importlib
import sys

from flask import Flask
from flask_restful import Api
from settings import configs, database

app = Flask(__name__)
app.config.from_object(configs.config)

api = Api(app)

urls = importlib.import_module(configs.ROOT_URL)

for res, url in urls.urlpatterns:
    if urls.prefix_url is not None:
        url = urls.prefix_url + url
    api.add_resource(res, url)


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







