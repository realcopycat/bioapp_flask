# -*- coding: utf-8 -*-
from flask import Flask

import config
from pear_admin.api import register_api
from pear_admin.extensions import db, register_extensions
from pear_admin.extensions.init_script import register_script
from pear_admin.orms import DepartmentORM, RightsORM, RoleORM, UserORM
from pear_admin.views import register_blueprint


def create_app() -> Flask:
    app = Flask("pear-admin-flask")
    app.config.from_object(config)
    register_extensions(app)
    register_api(app)
    register_blueprint(app)

    # 开发模式下注册初始化数据库的指令
    if app.config.get("CONFIG_NAME") == "dev":
        register_script(app)

    return app
