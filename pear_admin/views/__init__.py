# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

view_bp = Blueprint("views", __name__)


@view_bp.get("/")
def index():
    return render_template("index.html")


@view_bp.get("/dashboard")
def console_view():
    return render_template("console/console1.html")


@view_bp.get("/user")
def user_view():
    return render_template("system/user.html")


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
