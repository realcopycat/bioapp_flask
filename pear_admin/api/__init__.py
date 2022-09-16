# -*- coding: utf-8 -*-
from flask import Blueprint, Flask

from pear_admin.utils.functools import register_rest_api_func

from .auth_api import login_api, logout_api
from .role_api import RoleApi
from .users_api import UserApi


def register_api(app: Flask):
    api = Blueprint("api", __name__, url_prefix="/api/private/v1")
    api.add_url_rule("/login", view_func=login_api, methods=["POST"])
    api.add_url_rule("/logout", view_func=logout_api, methods=["POST"])
    register_rest_api_func(api, UserApi, "user_api", "/user/", pk="uid")
    register_rest_api_func(api, RoleApi, "role_api", "/role/", pk="rid")
    app.register_blueprint(api)
