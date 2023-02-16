# -*- coding: utf-8 -*-
import copy
import json
from collections import OrderedDict
from io import BytesIO
from random import choices
from typing import List

from captcha.image import ImageCaptcha
from flask import (
    Blueprint,
    Flask,
    abort,
    make_response,
    redirect,
    render_template,
    request,
)
from flask_jwt_extended import get_current_user, jwt_required
from PIL import Image

from pear_admin.extensions import redis_client
from pear_admin.orms import DepartmentORM, PermissionORM, RoleORM, UserORM

view_bp = Blueprint("views", __name__)


def register_blueprint(app: Flask):
    app.register_blueprint(view_bp)


@view_bp.get("/")
@jwt_required(optional=True)
def index():
    user = get_current_user()
    if not user:
        return redirect("/login")
    return render_template("index.html")


@view_bp.get("/login")
def login():
    return render_template("login.html")


@view_bp.get("/login/captcha")
def gen_captcha_image():
    image_code = request.args.get("image_code")

    """生成验证码"""
    content = "0123456789"
    image = ImageCaptcha()
    # 获取字符串
    code = "".join(choices(content, k=4))
    redis_client.set(f"image_code_{image_code}", code, ex=60)
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
    roles: List[RoleORM] = RoleORM.query.all()
    return render_template("system/user/user_add.html", roles=roles)


@view_bp.get("/user/edit")
def user_edit_view():
    uid = request.args.get("uid", type=int)
    if not uid:
        return abort(404)
    user: UserORM = UserORM.query.get(uid)
    roles: List[RoleORM] = RoleORM.query.all()
    return render_template("system/user/user_edit.html", user=user, roles=roles)


@view_bp.get("/role")
def role_view():
    return render_template("system/role/role.html")


@view_bp.get("/role/add")
def role_add_view():
    return render_template("system/role/role_add.html")


@view_bp.get("/role/edit/<int:rid>")
def role_edit_view(rid):
    role = RoleORM.query.get(rid)
    return render_template("system/role/role_edit.html", role=role)


@view_bp.get("/role/permission/<pid>")
def role_permission_view(pid):
    role: RoleORM = RoleORM.query.get(pid)
    # 获取权限列表的 id
    check_powers_list = [rp.id for rp in role.permission]

    permission: List[PermissionORM] = PermissionORM.query.all()
    permission_list = [
        {
            "id": item.id,
            "title": item.permission_name,
            "sort": item.sort or 0,
            "pid": item.pid,
            "spread": True,
            "checked": True if item.id in check_powers_list else False,
        }
        for item in permission
    ]
    permission_list.sort(key=lambda x: x["id"], reverse=True)
    menu_dict = OrderedDict()
    for _dict in permission_list:
        if _dict["id"] in menu_dict.keys():
            _dict["children"] = copy.deepcopy(menu_dict[_dict["id"]])
            _dict["children"].sort(key=lambda item: item["sort"])
            del menu_dict[_dict["id"]]

        if _dict["pid"] not in menu_dict:
            menu_dict[_dict["pid"]] = [_dict]
        else:
            menu_dict[_dict["pid"]].append(_dict)
    data = json.dumps(menu_dict.get(0))
    return render_template("system/role/role_permission.html", data=data, role=role)


@view_bp.get("/permission")
def permission_view():
    return render_template("system/permission/permission.html")


@view_bp.get("/permission/add")
def permission_add_view():
    return render_template("system/permission/permission_add.html")


@view_bp.get("/permission/edit/<int:pid>")
def permission_edit_view(pid):
    permission = PermissionORM.query.filter_by(id=pid).first()
    icon = str(permission.icon).split()
    if len(icon) == 2:
        icon = icon[1]
    else:
        icon = None
    return render_template(
        "system/permission/permission_edit.html", permission=permission, icon=icon
    )


@view_bp.get("/department")
def department_view():
    return render_template("system/department/department.html")


@view_bp.get("/department/add")
def department_add_view():
    return render_template("system/department/department_add.html")


@view_bp.get("/department/edit")
def department_edit_view():
    did = request.args.get("did", type=int)
    department: DepartmentORM = DepartmentORM.query.get(did)
    return render_template(
        "system/department/department_edit.html", department=department
    )


@view_bp.get("/echarts/line")
def echarts_line_view():
    return render_template("echarts/line.html")


@view_bp.get("/echarts/column")
def echarts_column_view():
    return render_template("echarts/column.html")


@view_bp.get("/person")
def person_view():
    return render_template("system/person/person.html")


@view_bp.get("/person/profile")
def person_profile_view():
    return render_template("system/person/profile.html")
