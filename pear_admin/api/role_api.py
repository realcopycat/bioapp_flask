# -*- coding: utf-8 -*-

from typing import List

from flask import request
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_pydantic import validate
from flask_sqlalchemy import Pagination
from pydantic import BaseModel, Field

from pear_admin.extensions import db
from pear_admin.models import PermissionORM, RoleORM


class RoleApi(MethodView):
    class PaginationModel(BaseModel):
        query: str = Field(default="")
        page: int = Field(default=1)
        pre_page: int = Field(default=10)

    class RoleModel(BaseModel):
        name: str = Field(default="")
        desc: str = Field(default="")

    @validate()
    def get(self, rid, query: PaginationModel):

        filters = []
        if query.query:
            filters.append(RoleORM.username.like("%" + query.query + "%"))

        paginate: Pagination = RoleORM.query.filter(*filters).paginate(
            page=query.page, per_page=query.pre_page
        )
        items: List[RoleORM] = paginate.items
        return {
            "result": {
                "total": paginate.total,
                "page": paginate.page,
                "pre_page": paginate.per_page,
                "roles": [
                    {
                        "id": item.id,
                        "name": item.name,
                        "desc": item.desc,
                    }
                    for item in items
                ],
            },
            "meta": {
                "message": "查询数据成功",
                "status": "success",
            },
        }

    @validate()
    def post(self, body: RoleModel):
        role = RoleORM()
        role.name = body.name
        role.desc = body.desc
        db.session.add(role)
        db.session.commit()
        return {
            "meta": {
                "message": "添加数据成功",
                "status": "success",
            },
        }

    @validate()
    def put(self, rid, body: RoleModel):
        role = RoleORM.query.get(rid)
        role.name = body.name
        role.desc = body.desc
        db.session.commit()
        return {
            "meta": {
                "message": "编辑角色数据成功",
                "status": "success",
            },
        }

    @validate()
    def delete(self, rid):
        if rid in [1, 2, 3]:
            return {
                "meta": {
                    "message": "测试数据禁止删除",
                    "status": "fail",
                },
            }
        role = RoleORM.query.get(rid)
        db.session.delete(role)
        db.session.commit()
        return {
            "meta": {
                "message": "删除角色数据成功",
                "status": "success",
            },
        }


class PermissionApi(MethodView):
    class PermissionModel(BaseModel):
        pid: int
        name: str
        code: str
        level: str
        path: str
        open_type: str
        icon: str
        sort: int

    def get(self, pid):
        if pid:
            permission: PermissionORM = PermissionORM.query.get(pid)
            return {
                "result": {
                    "permission": [
                        {
                            "id": permission.id,
                            "pid": permission.pid,
                            "level": permission.level,
                            "name": permission.name,
                            "code": permission.code,
                            "icon": permission.icon,
                            "path": permission.path,
                            "open_type": permission.open_type,
                            "enable": permission.enable,
                            "sort": permission.sort,
                        }
                    ],
                },
                "meta": {
                    "message": "查询数据成功",
                    "status": "success",
                },
            }
        else:
            permission_list: List[PermissionORM] = PermissionORM.query.all()
            _type = request.args.get("type")
            if _type == "dtree":
                rets = [
                    {
                        "id": permission.id,
                        "pid": permission.pid,
                        "level": permission.level,
                        "name": permission.name,
                        "code": permission.code,
                        "icon": permission.icon,
                        "path": permission.path,
                        "open_type": permission.open_type,
                        "enable": permission.enable,
                        "sort": permission.sort or 0,
                    }
                    for permission in permission_list
                ]
                rets.append({"id": 0, "name": "顶级权限", "pid": -1})
                return {
                    "status": {"code": 200, "message": "默认"},  # 兼容 dtree
                    "data": rets,
                }
            return {
                "result": {
                    "permission_list": [
                        {
                            "id": permission.id,
                            "pid": permission.pid,
                            "level": permission.level,
                            "name": permission.name,
                            "code": permission.code,
                            "icon": permission.icon,
                            "path": permission.path,
                            "open_type": permission.open_type,
                            "enable": permission.enable,
                            "sort": permission.sort or 0,
                        }
                        for permission in permission_list
                    ],
                },
                "meta": {
                    "message": "查询数据成功",
                    "status": "success",
                },
            }

    @validate()
    def post(self, body: PermissionModel):
        permission = PermissionORM()
        permission.pid = body.pid
        permission.name = body.name
        permission.code = body.code
        permission.level = body.level
        permission.path = body.path
        permission.open_type = body.open_type
        permission.icon = body.icon
        permission.sort = body.sort
        db.session.add(permission)
        db.session.commit()
        return {
            "meta": {
                "message": "添加数据成功",
                "status": "success",
            },
        }

    @validate()
    def put(self, pid, body: PermissionModel):
        if pid <= 11:
            return {
                "meta": {
                    "message": "默认数据禁止修改",
                    "status": "fail",
                },
            }
        permission = PermissionORM.query.get(pid)
        permission.pid = body.pid
        permission.name = body.name
        permission.code = body.code
        permission.level = body.level
        permission.path = body.path
        permission.open_type = body.open_type
        permission.icon = body.icon
        permission.sort = body.sort
        db.session.add(permission)
        db.session.commit()
        return {
            "meta": {
                "message": "修改权限数据成功",
                "status": "success",
            },
        }

    @validate()
    def delete(self, pid):
        if pid <= 11:
            return {
                "meta": {
                    "message": "测试数据禁止删除",
                    "status": "fail",
                },
            }
        permission = PermissionORM.query.get(pid)
        db.session.delete(permission)
        db.session.commit()
        return {
            "meta": {
                "message": "删除权限数据成功",
                "status": "success",
            },
        }


def role_permission(rid):
    role: RoleORM = RoleORM.query.get(rid)
    ids: str = request.json.get("ids")
    per_arr = PermissionORM.query.filter(PermissionORM.id.in_(ids.split(","))).all()
    role.permission = []
    role.permission = per_arr
    role.permission_ids = ids
    db.session.commit()
    return {
        "meta": {
            "message": "修改角色权限成功",
            "status": "success",
        },
    }


def permission_enable(pid):
    permission = PermissionORM.query.get(pid)
    enable = request.json.get("enable")
    permission.enable = enable
    db.session.commit()
    return {
        "meta": {
            "message": "修改权限状态成功",
            "status": "success",
        },
    }
