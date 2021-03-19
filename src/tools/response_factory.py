from flask import make_response
from .serializer import DHLEncoder
import json

def create_response(payload):
    result = dict(data=payload,error_code=0)
    content = json.dumps(result, cls=DHLEncoder, ensure_ascii=False, indent=4)
    resp = make_response(content)
    resp.mimetype = "application/json"
    return resp