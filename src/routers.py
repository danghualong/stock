from .stat import stat_bp

def init_app(app):
    app.register_blueprint(stat_bp)