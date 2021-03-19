from .model import APIException, ServerError
from werkzeug.exceptions import HTTPException
from .logger import currentLogger

def init_app(app):
    @app.errorhandler(Exception)
    def framework_error(e):
        currentLogger.error("error info: %s" % e) # 对错误进行日志记录
        if isinstance(e, APIException):
            return e
        if isinstance(e, HTTPException):
            code = e.code
            msg = e.description
            error_code = 1007
            return APIException(error_code, msg, code)
        else:
            if not app.config['DEBUG']:
                return ServerError()
            else:
                return e