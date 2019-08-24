import os

from flask_restful import Resource
from flask import send_file, abort
from urllib.parse import quote
from log import create_logger

class ImgProcess(Resource):
    logger = create_logger(__name__)

    def get(self, img_type, img_date, filename):
        img_path = os.path.join("images", img_type, img_date, filename)
        # /images/<string:img_type>/<string:img_date>/<string:filename>'
        attachement_name = quote(filename)
        isfile = os.path.isfile(img_path)
        self.logger.info(img_path)
        self.logger.info(isfile)
        if not isfile:
            return abort(404)

        return send_file(img_path, attachment_filename=attachement_name)

