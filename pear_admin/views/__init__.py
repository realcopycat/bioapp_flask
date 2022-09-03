# -*- coding: utf-8 -*-
from flask import Blueprint, abort, render_template, request

from pear_admin.models import UserORM

view_bp = Blueprint("views", __name__)


@view_bp.get("/")
def index():
    return render_template("index.html")


@view_bp.get("/login")
def login():
    return render_template("login.html")


@view_bp.get("/dashboard")
def console_view():
    return render_template("console/console1.html")


@view_bp.get("/user")
def user_view():
    return render_template("system/user/user.html")


@view_bp.get("/user/add")
def user_add_view():
    return render_template("system/user/user_add.html")


@view_bp.get("/user/edit")
def user_edit_view():
    uid = request.args.get("uid", type=int)
    if not uid:
        return abort(404)
    user = UserORM.query.get(uid)
    return render_template("system/user/user_edit.html", user=user)


@view_bp.get("/role")
def role_view():
    return render_template("system/role.html")


@view_bp.get("/permission")
def permission_view():
    return render_template("system/permission.html")


@view_bp.get("/department")
def department_view():
    return render_template("system/department.html")


@view_bp.get("/sys_log")
def sys_log_view():
    return render_template("system/sys_log.html")


@view_bp.get("/echarts/line")
def echarts_line_view():
    return render_template("echarts/line.html")


@view_bp.get("/echarts/column")
def echarts_column_view():
    return render_template("echarts/column.html")


@view_bp.get("/person")
def person_view():
    return render_template("system/person.html")
