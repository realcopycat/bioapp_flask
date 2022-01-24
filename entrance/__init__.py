from flask import Flask
import os
from common.extend.logger import config_logger
from entrance.bps import sys, register_parent_bp
from entrance.extensions import init_extensions


def create_app():
    config_logger()
    app = Flask(__name__)
    app.config.from_pyfile('config/config.py')
    register_parent_bp(app)
    init_extensions(app)
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        print(
            """

              ___                  _      _       _        ___ _         _   
             | _ \___ __ _ _ _    /_\  __| |_ __ (_)_ _   | __| |__ _ __| |__
             |  _/ -_) _` | '_|  / _ \/ _` | '  \| | ' \  | _|| / _` (_-< / /
             |_| \___\__,_|_|   /_/ \_\__,_|_|_|_|_|_||_| |_| |_\__,_/__/_\_\\


            """
        )

    return app
