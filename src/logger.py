import logging
import os
from logging.handlers import RotatingFileHandler

def init_app(app):
    baseDir=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(filename)s--%(funcName)s(%(lineno)s):%(message)s')
    dir=os.path.join(baseDir,'logs')
    if(not os.path.exists(dir)):
        os.mkdir(dir)
    fh=RotatingFileHandler(os.path.join(dir,'mylog.log'),maxBytes=10*1024*1024,backupCount=5)
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)
    currentLogger.addHandler(fh)
    app.logger = currentLogger

def _getLogger():
    logger = logging.getLogger("default")
    logger.setLevel(logging.INFO)
    return logger

currentLogger=_getLogger()