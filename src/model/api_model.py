from werkzeug.exceptions import HTTPException
from werkzeug.wrappers.response import Response
import json


class JsonResult(object):
    code = 200
    error_code = 0
    data = None

    def __init__(self, data):
        self.data = data
    
    def getHeaders(self):
        return [('Content-Type', 'application/json')]
    def getBody(self):
        pass


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
        super(HTTPException, self).__init__(self.msg)
    
    def get_body(self, environ=None):
        body = dict(
            msg=self.msg,
            error_code=self.error_code)
        return json.dumps(body)
    
    def get_headers(self, environ=None):
        """Get a list of headers."""
        return [('Content-Type', 'application/json')]
    
class BadRequest(APIException):
    pass
    