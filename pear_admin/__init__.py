__version__ = "0.1.0"
from flask import Flask

from pear_admin.views import view_bp


def create_app():
    app = Flask("pear-admin-flask")
    app.register_blueprint(view_bp)
    return app
