# -*- coding: utf-8 -*-
from flask import make_response, request
from flask_jwt_extended import create_access_token, jwt_required

from pear_admin.models import UserORM


def login_api():
    username = request.json.get("username")
    password = request.json.get("password")

    user: UserORM = UserORM.query.filter(UserORM.username == username).one_or_none()
    if not user:
        return {
            "meta": {
                "status": "fail",
                "message": "没有查询到此用户",
            }
        }, 401
    if not user.check_password(password):
        return {
            "meta": {
                "status": "fail",
                "message": "用户密码错误",
            }
        }, 401

    access_token = create_access_token(identity=user)
    response = make_response(
        {
            "result": {"access_token": access_token},
            "meta": {
                "status": "success",
                "message": "用户登录成功",
            },
        }
    )
    response.set_cookie("is_login", "true")
    return response


@jwt_required()
def logout_api():
    response = make_response(
        {
            "meta": {
                "status": "success",
                "message": "用户退出成功",
            },
        }
    )
    response.set_cookie("is_login", "")
    return response
