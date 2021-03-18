from flask import Flask
import os
from .settings import configs
from . import cron, logger, db


def createApp(configName=None):
    app = Flask(__name__)
    if configName == None:
        configName = os.getenv("FLASK_ENV", "production")
    app.config.from_object(configs[configName])
    logger.init_app(app)
    db.init_app(app)
    cron.init_app(app)
    return app
