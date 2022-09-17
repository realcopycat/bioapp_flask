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
