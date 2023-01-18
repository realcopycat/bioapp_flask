from applications import create_app
from flask_migrate import Migrate
from applications.extensions import db

from gevent import pywsgi

import os

app = create_app()

migrate = Migrate(app, db)

if __name__ == '__main__':
    # app.run()
    server = pywsgi.WSGIServer((os.getenv('FLASK_RUN_HOST'), int(os.getenv('FLASK_RUN_PORT'))), app, log=None)
    server.serve_forever()
