from flask import Flask

from entrance import config
from entrance.bps import sys, register_parent_bp


from entrance.extensions import init_extensions


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    register_parent_bp(app)
    init_extensions(app)
    return app
