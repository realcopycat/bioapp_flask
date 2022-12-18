# -*- coding: utf-8 -*-

from flask import request
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_pydantic import validate
from flask_sqlalchemy import Pagination

from pear_admin.models import PaginationModel, PermissionModel, RoleModel
from pear_admin.orms import PermissionORM, RoleORM
from pear_admin.utils.response_code import RetCode


class RoleApi(MethodView):
    @validate()
    def get(self, rid, query: PaginationModel):
        filters = []
        if query.query:
            filters.append(RoleORM.username.like("%" + query.query + "%"))

        paginate: Pagination = RoleORM.query.filter(*filters).paginate(
            page=query.page, per_page=query.pre_page
        )
        items: list[RoleORM] = paginate.items
        return {
            "result": {
                "total": paginate.total,
                "page": paginate.page,
                "pre_page": paginate.per_page,
                "roles": [item.json() for item in items],
            },
            "meta": {
                "code": RetCode.OK.value,
                "message": "查询数据成功",
                "status": "success",
            },
        }

    @jwt_required()
    @validate()
    def post(self, body: RoleModel):
        role = RoleORM()
        role.name = body.name
        role.desc = body.desc
        role.save_to_db()
        return {
            "meta": {
                "code": RetCode.OK.value,
                "message": "添加数据成功",
                "status": "success",
            },
        }

    @jwt_required()
    @validate()
    def put(self, rid, body: RoleModel):
        role = RoleORM.query.get(rid)
        role.name = body.name
        role.desc = body.desc
        role.save_to_db()
        return {
            "meta": {
                "code": RetCode.OK.value,
                "message": "编辑角色数据成功",
                "status": "success",
            },
        }

    @jwt_required()
    @validate()
    def delete(self, rid):
        # 用户项目演示
        if rid in [1, 2, 3]:
            return {
                "meta": {
                    "code": RetCode.DELETE_ERR.value,
                    "message": RetCode.DELETE_ERR.errmsg,
                    "status": "fail",
                },
            }
        role: RoleORM = RoleORM.find_by_id(rid)
        role.delete_from_db()
        return {
            "meta": {
                "code": 0,
                "message": "删除角色数据成功",
                "status": "success",
            },
        }


class PermissionApi(MethodView):
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
            permission_list: list[PermissionORM] = PermissionORM.query.all()
            _type = request.args.get("type")
            if _type == "dtree":
                rets = [permission.json() for permission in permission_list]
                rets.append({"id": 0, "name": "顶级权限", "pid": -1})
                return {
                    "status": {"code": 200, "message": "默认"},  # 兼容 dtree
                    "data": rets,
                }
            return {
                "result": {
                    "permission_list": [
                        permission.json() for permission in permission_list
                    ],
                },
                "meta": {
                    "message": "查询数据成功",
                    "status": "success",
                },
            }

    @jwt_required()
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
        permission.save_to_db()
        return {
            "meta": {
                "message": "添加数据成功",
                "status": "success",
            },
        }

    @jwt_required()
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
        permission.save_to_db()
        return {
            "meta": {
                "message": "修改权限数据成功",
                "status": "success",
            },
        }

    @jwt_required()
    @validate()
    def delete(self, pid):
        if pid <= 11:
            return {
                "meta": {
                    "message": "测试数据禁止删除",
                    "status": "fail",
                },
            }
        permission: PermissionORM = PermissionORM.query.get(pid)
        permission.delete_from_db()
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
    role.save_to_db()
    return {
        "meta": {
            "message": "修改角色权限成功",
            "status": "success",
        },
    }


def permission_enable(pid):
    permission = PermissionORM.find_by_id(pid)
    enable = request.json.get("enable")
    permission.enable = enable
    permission.save_to_db()
    return {
        "meta": {
            "message": "修改权限状态成功",
            "status": "success",
        },
    }
