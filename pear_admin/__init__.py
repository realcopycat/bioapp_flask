# -*- coding: utf-8 -*-
from flask import Flask

import config
from pear_admin.api import register_api
from pear_admin.extensions import db, register_extensions
from pear_admin.models import DepartmentORM, PermissionORM, RoleORM, UserORM
from pear_admin.views import view_bp


def create_app() -> Flask:
    app = Flask("pear-admin-flask")
    app.config.from_object(config)
    register_extensions(app)
    register_api(app)
    app.register_blueprint(view_bp)

    @app.cli.command()
    def create():
        init_databases()

    return app


def init_databases():
    db.drop_all()
    db.create_all()

    department_list = [
        {
            "id": 1,
            "pid": 0,
            "name": "集团总部",
            "sort": 1,
            "leader": "集团负责人",
            "phone": "12312345679",
            "email": "123qq.com",
            "enable": 1,
            "comment": "",
            "address": "这是集团总部",
        },
        {
            "id": 4,
            "pid": 1,
            "name": "济南分公司",
            "sort": 2,
            "leader": "就眠仪式",
            "phone": "12312345678",
            "email": "1234qq.com",
            "enable": 1,
            "comment": "",
            "address": "这是济南",
        },
        {
            "id": 5,
            "pid": 1,
            "name": "唐山分公司",
            "sort": 4,
            "leader": "mkg",
            "phone": "12312345678",
            "email": "123@qq.com",
            "enable": 1,
            "comment": "",
            "address": "这是唐山",
        },
        {
            "id": 7,
            "pid": 4,
            "name": "济南分公司-开发部",
            "sort": 5,
            "leader": "就眠仪式",
            "phone": "12312345678",
            "email": "123@qq.com",
            "enable": 1,
            "comment": "",
            "address": "测试",
        },
        {
            "id": 8,
            "pid": 5,
            "name": "唐山分公司-测试部",
            "sort": 6,
            "leader": "mkg",
            "phone": "12312345678",
            "email": "123@qq.com",
            "enable": 1,
            "comment": "",
            "address": "测试部",
        },
        {
            "id": 9,
            "pid": 1,
            "name": "长沙分公司",
            "sort": 6,
            "leader": "正心全栈编程",
            "phone": "18675867241",
            "email": "pyxxp@qq.com",
            "enable": 1,
            "comment": "",
            "address": "湖南省长沙市望城区",
        },
        {
            "id": 10,
            "pid": 9,
            "name": "长沙分公司-VIP服务中心",
            "sort": 6,
            "leader": "正心全栈编程",
            "phone": "18675867241",
            "email": "pyxxp@qq.com",
            "enable": 1,
            "comment": "",
            "address": "",
        },
        {
            "id": 11,
            "pid": 9,
            "name": "长沙分公司-招生中心",
            "sort": 6,
            "leader": "正心全栈编程",
            "phone": "18675867241",
            "email": "pyxxp@qq.com",
            "enable": 1,
            "comment": "",
            "address": "",
        },
        {
            "id": 12,
            "pid": 9,
            "name": "长沙分公司-运营中心",
            "sort": 6,
            "leader": "正心全栈编程",
            "phone": "18675867241",
            "email": "pyxxp@qq.com",
            "enable": 1,
            "comment": "",
            "address": "",
        },
    ]
    for department in department_list:
        department_obj = DepartmentORM()
        for key, value in department.items():
            setattr(department_obj, key, value)
        db.session.add(department_obj)
    db.session.commit()

    permission_list = [
        {
            "id": 1,
            "name": "工作空间",
            "level": 0,
            "icon": "layui-icon layui-icon-console",
            "path": "",
            "pid": 0,
        },
        {
            "id": 2,
            "name": "控制后台",
            "level": 1,
            "icon": "layui-icon layui-icon-console",
            "path": "/dashboard",
            "pid": 1,
            "open_type": "_iframe",
        },
        {
            "id": 3,
            "name": "系统管理",
            "level": 0,
            "icon": "layui-icon layui-icon-set-fill",
            "path": "",
            "pid": 0,
        },
        {
            "id": 4,
            "name": "用户管理",
            "level": 1,
            "icon": "layui-icon layui-icon-face-smile",
            "path": "/user",
            "pid": 3,
            "open_type": "_iframe",
        },
        {
            "id": 5,
            "name": "角色管理",
            "level": 1,
            "icon": "layui-icon layui-icon-face-cry",
            "path": "/role",
            "pid": 3,
            "open_type": "_iframe",
        },
        {
            "id": 6,
            "name": "权限管理",
            "level": 1,
            "icon": "layui-icon layui-icon-face-cry",
            "path": "/permission",
            "pid": 3,
            "open_type": "_iframe",
        },
        {
            "id": 7,
            "name": "部门管理",
            "level": 1,
            "icon": "layui-icon layui-icon-face-cry",
            "path": "/department",
            "pid": 3,
            "open_type": "_iframe",
        },
        {
            "id": 8,
            "name": "行为日志",
            "level": 1,
            "icon": "layui-icon layui-icon-face-cry",
            "path": "/sys_log",
            "pid": 3,
            "open_type": "_iframe",
        },
        {
            "id": 9,
            "name": "数据图表",
            "level": 0,
            "icon": "layui-icon layui-icon-chart",
            "path": "",
            "pid": 0,
        },
        {
            "id": 10,
            "name": "折线图",
            "level": 1,
            "icon": "layui-icon layui-icon-face-cry",
            "path": "/echarts/line",
            "pid": 9,
            "open_type": "_iframe",
        },
        {
            "id": 11,
            "name": "柱状图",
            "level": 1,
            "icon": "layui-icon layui-icon-face-smile",
            "path": "/echarts/column",
            "pid": 9,
            "open_type": "_iframe",
        },
    ]
    for permission in permission_list:
        permission_obj = PermissionORM()
        for key, value in permission.items():
            setattr(permission_obj, key, value)
        db.session.add(permission_obj)
    db.session.commit()

    role_list = [
        {
            "id": 1,
            "name": "超级管理员",
            "desc": "超级管理员",
        },
        {
            "id": 2,
            "name": "普通管理员",
            "desc": "普通管理员",
        },
        {
            "id": 3,
            "name": "普通用户",
            "desc": "普通用户",
        },
    ]
    for role in role_list:
        role_obj = RoleORM()
        for key, value in role.items():
            setattr(role_obj, key, value)
        db.session.add(role_obj)
    db.session.commit()
    role_permission_items = {
        1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        2: [1, 2, 3, 4, 8, 9, 10, 11],
        3: [1, 2, 9, 10, 11],
    }
    for role_id, role_per_ids in role_permission_items.items():
        role_obj: RoleORM = RoleORM.query.get(role_id)
        role_obj.permission_ids = ",".join(map(str, role_per_ids))
        per_list = PermissionORM.query.filter(PermissionORM.id.in_(role_per_ids)).all()
        role_obj.permission = per_list
    db.session.commit()

    user_list = [
        {
            "id": 1,
            "username": "admin",
            "nickname": "超级管理员",
            "password": "123456",
            "email": "8540854@qq.com",
            "avatar": "",
            "mobile": "15543526531",
            "gender": "男",
            "state": True,
        },
        {
            "id": 2,
            "username": "就眠仪式",
            "nickname": "就眠仪式",
            "password": "123456",
            "email": "8540854@qq.com",
            "avatar": "",
            "mobile": "155324324234",
            "gender": "男",
            "state": True,
        },
        {
            "id": 3,
            "username": "zhengxinonly",
            "nickname": "正心全栈编程",
            "password": "123456",
            "email": "pyxxponly@gmail.com",
            "avatar": "",
            "mobile": "18675867241",
            "gender": "男",
            "state": True,
        },
    ]
    for user in user_list:
        user_obj = UserORM()
        for key, value in user.items():
            if key == "password":
                user_obj.password = value
            else:
                setattr(user_obj, key, value)
        user_obj.role.append(RoleORM.query.get(user_obj.id))
        db.session.add(user_obj)
    db.session.commit()
