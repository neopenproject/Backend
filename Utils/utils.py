from werkzeug.utils import secure_filename
from datetime import datetime as dt
import os


def set_response(code, result):
    return {"code": code, "result": result}


def upload_img(path, file):
    now = dt.now()
    date_path = now.strftime("%Y-%m-%d")

    filename = secure_filename(file.filename)

    current_date = str(int(now.timestamp() * 1000000))
    filename = "{}{}".format(current_date, filename)

    upload_text = os.path.join(path, date_path, filename)
    file.save(upload_text)
    return upload_text

