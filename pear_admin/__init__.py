# -*- coding: utf-8 -*-
from flask import Flask

import config
from pear_admin.api import register_api
from pear_admin.extensions import db, register_extensions
from pear_admin.orms import DepartmentORM, PermissionORM, RoleORM, UserORM
from pear_admin.views import register_blueprint


def create_app() -> Flask:
    app = Flask("pear-admin-flask")
    app.config.from_object(config)
    register_extensions(app)
    register_api(app)
    register_blueprint(app)

    return app
