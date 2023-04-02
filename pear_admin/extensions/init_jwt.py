from flask import Flask, redirect, request
from flask_jwt_extended import JWTManager

jwt = JWTManager()


def register_jwt(app: Flask):
    from pear_admin.orms import UserORM

    jwt.init_app(app)

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

        return {
            "status": "fail",
            "message": "token 已失效",
        }, 401
