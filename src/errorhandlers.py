from .model import APIException, ServerError
from werkzeug.exceptions import HTTPException
from .logger import currentLogger
from flask import request

def init_app(app):
    @app.errorhandler(Exception)
    def framework_error(e):
        currentLogger.error("url is {0},error info:{1}".format(request.path,e) if isinstance(e, HTTPException) else "error info:{0}".format(e)) # 对错误进行日志记录
        if isinstance(e, APIException):
            return e
        if isinstance(e, HTTPException):
            msg = e.description
            error_code = 1007
            return APIException(error_code, msg)
        else:
            if not app.config['DEBUG']:
                return ServerError()
            else:
                return e