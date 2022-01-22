from flask import Flask

from entrance.extend.restx import sys
# from entrance.extensions import init_extensions


def create_app():
    app = Flask(__name__)
    app.register_blueprint(sys)
    # init_extensions(app)
    return app
