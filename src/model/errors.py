from werkzeug.exceptions import HTTPException
import json

class APIException(HTTPException):
    code = 200
    error_code = 999
    msg = "unknown error"

    def __init__(self,error_code=None, msg=None, code=None):
        if (code):
            self.code = code
        if (msg):
            self.msg = msg
        if (error_code):
            self.error_code = error_code
        super(APIException, self).__init__(self.msg,None)
    
    def get_body(self, environ=None):
        body = dict(
            msg=self.msg,
            error_code=self.error_code)
        return json.dumps(body)
    
    def get_headers(self, environ=None):
        """Get a list of headers."""
        return [('Content-Type', 'application/json')]
    
class NoFound(APIException):
    error_code = 404
    msg = "当前地址不存在"

class ServerError(APIException):
    msg = 'sorry, we made a mistake!'
    error_code = 999  