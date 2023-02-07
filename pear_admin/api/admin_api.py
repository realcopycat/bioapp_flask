from collections import OrderedDict
from copy import deepcopy

from flask import make_response, request
from flask_jwt_extended import jwt_required

from pear_admin.orms import PermissionORM

# 生成菜单树


@jwt_required()
def menus_api():
    permission_orm_list = PermissionORM.query.filter(
        PermissionORM.permission_type != "auth"
    ).all()
    permission_list = [
        permission_orm.menu_json() for permission_orm in permission_orm_list
    ]
    permission_list.sort(key=lambda x: (x["pid"], x["id"]), reverse=True)

    menu_dict_list = OrderedDict()
    for menu_dict in permission_list:
        if menu_dict["permission_id"] in menu_dict_list.keys():  # 如果当前节点已经存在与字典中
            # 当前节点添加子节点
            menu_dict["children"] = deepcopy(menu_dict_list[menu_dict["permission_id"]])
            menu_dict["children"].sort(key=lambda item: item["sort"])
            # 删除子节点
            del menu_dict_list[menu_dict["permission_id"]]

        if menu_dict["pid"] not in menu_dict_list:
            menu_dict_list[menu_dict["pid"]] = [menu_dict]
        else:
            menu_dict_list[menu_dict["pid"]].append(menu_dict)
    return sorted(menu_dict_list.get(0), key=lambda item: item["sort"])
    return [
        {
            "id": 1,
            "title": "工作空间",
            "icon": "layui-icon layui-icon-console",
            "type": 0,
            "href": "",
            "children": [
                {
                    "id": 10,
                    "title": "控制后台",
                    "icon": "layui-icon layui-icon-console",
                    "type": 1,
                    "openType": "_iframe",
                    "href": "/dashboard",
                }
            ],
        },
        {
            "id": "system",
            "title": "系统管理",
            "icon": "layui-icon layui-icon-set-fill",
            "type": 0,
            "href": "",
            "children": [
                {
                    "id": 603,
                    "title": "权限管理",
                    "icon": "layui-icon layui-icon-face-cry",
                    "type": 1,
                    "openType": "_iframe",
                    "href": "/permission",
                },
                {
                    "id": 602,
                    "title": "角色管理",
                    "icon": "layui-icon layui-icon-face-cry",
                    "type": 1,
                    "openType": "_iframe",
                    "href": "/role",
                },
                {
                    "id": 604,
                    "title": "部门管理",
                    "icon": "layui-icon layui-icon-face-cry",
                    "type": 1,
                    "openType": "_iframe",
                    "href": "/department",
                },
                {
                    "id": 601,
                    "title": "用户管理",
                    "icon": "layui-icon layui-icon-face-smile",
                    "type": 1,
                    "openType": "_iframe",
                    "href": "/user",
                },
            ],
        },
        {
            "id": "echarts",
            "title": "数据图表",
            "icon": "layui-icon layui-icon-chart",
            "type": 0,
            "href": "",
            "children": [
                {
                    "id": 12121,
                    "title": "折线图",
                    "icon": "layui-icon layui-icon-face-smile",
                    "type": 1,
                    "openType": "_iframe",
                    "href": "/echarts/line",
                },
                {
                    "id": 121212,
                    "title": "柱状图",
                    "icon": "layui-icon layui-icon-face-smile",
                    "type": 1,
                    "openType": "_iframe",
                    "href": "/echarts/column",
                },
            ],
        },
    ]
