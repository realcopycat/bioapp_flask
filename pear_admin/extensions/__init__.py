# -*- coding: utf-8 -*-
from flask import Flask, jsonify, redirect, request
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from pear_admin.utils.flask_redis import FlaskRedis

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
redis_client = FlaskRedis(decode_responses=True)




def register_extensions(app: Flask) -> None:
    from pear_admin import UserORM

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    redis_client.init_app(app)

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return UserORM.query.filter_by(id=identity).one_or_none()

    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user.id

    @jwt.expired_token_loader
    def my_expired_token_callback(jwt_header, jwt_payload):
        if request.method == "GET":
            return redirect("/login")

        return (
            jsonify(
                meta={
                    "status": "fail",
                    "message": "token 已失效",
                }
            ),
            401,
        )
