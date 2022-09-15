# -*- coding: utf-8 -*-
from io import BytesIO
from random import choices

from captcha.image import ImageCaptcha
from flask import Blueprint, abort, make_response, redirect, render_template, request
from PIL import Image

from pear_admin.models import UserORM

view_bp = Blueprint("views", __name__)


@view_bp.get("/")
def index():
    is_login = request.cookies.get("is_login")
    if is_login != "true":
        return redirect("/login")
    return render_template("index.html")


@view_bp.get("/login")
def login():
    return render_template("login.html")


@view_bp.get("/login/captcha")
def gen_captcha_image():
    """生成验证码"""
    content = "0123456789"
    image = ImageCaptcha()
    # 获取字符串
    code = "".join(choices(content, k=4))
    # 生成图像
    image = Image.open(image.generate(code))
    out = BytesIO()
    image.save(out, "png")
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = "image/png"
    return resp


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
