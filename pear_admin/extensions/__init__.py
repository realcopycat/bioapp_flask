# -*- coding: utf-8 -*-
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from pear_admin.utils.flask_redis import FlaskRedis

from .init_jwt import register_jwt

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
redis_client = FlaskRedis(decode_responses=True)


def register_extensions(app: Flask) -> None:
    db.init_app(app)
    migrate.init_app(app, db)
    redis_client.init_app(app)
    register_jwt(app)
