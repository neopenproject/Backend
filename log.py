import logging
import os
from settings.configs import MODE, BASE_DIR, FORMAT_STRING

# DEBUG     개발용
# INFO      이벤트 보고
# WARING    수정이 필요한 문제
# ERROR     일부기능 문제
# CRITICAL  심각한 문제

if MODE == "REAL":
    numeric_level = getattr(logging, 'INFO', None)
else:
    numeric_level = getattr(logging, 'DEBUG', None)

if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: {MODE}'.format(MODE))

formatter = logging.Formatter(FORMAT_STRING)


def create_logger(name):
    logger = logging.getLogger(name)

    if len(logger.handlers) > 0:
        return logger

    logger.setLevel(numeric_level)

    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(os.path.join(BASE_DIR, 'logs', 'server.log'))

    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    logger.propagate = 0
    return logger

