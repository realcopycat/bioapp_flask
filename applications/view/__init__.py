from flask import Flask

from .index import index_bp
from .logs_view import logs_bp
from .roles import role_bp
from .system_view import system_bp
from .document_view import document_bp

from . import department
from . import file
from . import rights
from . import users


def init_view(app: Flask):
    app.register_blueprint(index_bp)
    app.register_blueprint(logs_bp)
    app.register_blueprint(role_bp)
    app.register_blueprint(system_bp)
    app.register_blueprint(document_bp)
