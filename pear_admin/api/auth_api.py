# -*- coding: utf-8 -*-

from flask import make_response, request
from flask.views import MethodView
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    set_access_cookies,
    set_refresh_cookies,
    unset_access_cookies,
    unset_refresh_cookies,
)

from pear_admin.extensions import redis_client
from pear_admin.orms import UserORM
from pear_admin.utils.response_code import RetCode


class LoginApi(MethodView):
    def post(self):
        nickname = request.json.get("nickname")
        password = request.json.get("password")
        captcha_code = request.json.get("captcha_code")
        image_code_uuid = request.json.get("image_code")

        user: UserORM = UserORM.find_by_nickname(nickname)

        code = redis_client.get(f"image_code_{image_code_uuid}")
        if code != captcha_code:
            return {
                "meta": {
                    "code": RetCode.CAPTCHA_CODE_ERR.code,
                    "status": "fail",
                    "message": RetCode.CAPTCHA_CODE_ERR.value,
                }
            }, 401
        if not user:
            return {
                "meta": {
                    "code": RetCode.USER_NOTFOUND_ERR.code,
                    "status": "fail",
                    "message": RetCode.USER_NOTFOUND_ERR.errmsg,
                }
            }, 401
        if not user.check_password(password):
            return {
                "meta": {
                    "code": RetCode.PWD_ERR.code,
                    "status": "fail",
                    "message": RetCode.PWD_ERR.errmsg,
                }
            }, 401

        access_token = create_access_token(identity=user)
        refresh_token = create_refresh_token(identity=user)
        response = make_response(
            {
                "result": {
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                },
                "meta": {
                    "code": RetCode.OK.code,
                    "status": "success",
                    "message": "用户登录成功",
                },
            }
        )
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)
        return response


class LogoutApi(MethodView):
    @jwt_required()
    def post(self):
        response = make_response(
            {
                "meta": {
                    "code": RetCode.OK.value,
                    "status": "success",
                    "message": "用户退出成功",
                },
            }
        )
        unset_access_cookies(response)
        unset_refresh_cookies(response)
        return response
