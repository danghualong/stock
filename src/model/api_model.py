from werkzeug.exceptions import HTTPException
from werkzeug.wrappers.response import Response



class JsonResult(object):
    code = 200
    error_code = 0
    data = None

    def __init__(self, data):
        self.data = data
    
    def getHeaders(self):
        return [('Content-Type', 'application/json')]
    def getBody(self):

    

class APIException(HTTPException):
    code = 200
    error_code = 999
    msg = "unknown error"

    def __init__(self, msg, error_code):
        if (msg):
            self.msg = msg
        if (error_code):
            self.error_code = error_code
        super(HTTPException, self).__init__(self.msg)
    
    