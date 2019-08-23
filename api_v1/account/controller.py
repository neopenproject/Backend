from flask_restful import Resource
from log import create_logger


class Index(Resource):
    __logger = create_logger(__name__)

    def get(self):
        self.__logger.debug('activation get method')
        return 'account get'

    def post(self):
        self.__logger.debug('activation post method')
        return 'account post'

    def delete(self):
        self.__logger.debug('activation delete method')
        return 'account delete'

    def put(self):
        self.__logger.debug('activation put method')
        return 'account put'
