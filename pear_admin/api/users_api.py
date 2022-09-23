# -*- coding: utf-8 -*-
import typing as t
from typing import List

from flask import request
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_pydantic import validate
from flask_sqlalchemy import Pagination
from pydantic import BaseModel, Field

from pear_admin.extensions import db
from pear_admin.models import DepartmentORM, PermissionORM, RoleORM, UserORM


class UserApi(MethodView):
    class PaginationModel(BaseModel):
        query: str = Field(default="")
        page: int = Field(default=1)
        pre_page: int = Field(default=10)

    class UserModel(BaseModel):
        username: str = Field(default="")
        nickname: str = Field(default="")
        password: str = Field(default="")
        mobile: str = Field(default="")
        email: str = Field(default="")
        gender: str = Field(default="")
        education: str = Field(default="")
        state: bool = Field(default=False)

    @validate()
    def get(self, uid, query: PaginationModel):

        filters = []
        if query.query:
            filters.append(UserORM.username.like("%" + query.query + "%"))

        paginate: Pagination = UserORM.query.filter(*filters).paginate(
            page=query.page, per_page=query.pre_page
        )
        items: List[UserORM] = paginate.items
        return {
            "result": {
                "total": paginate.total,
                "page": paginate.page,
                "pre_page": paginate.per_page,
                "users": [
                    {
                        "id": item.id,
                        "username": item.username,
                        "nickname": item.nickname,
                        "gender": item.gender,
                        "mobile": item.mobile,
                        "email": item.email,
                        "state": item.state,
                        "create_at": item.create_at,
                    }
                    for item in items
                ],
            },
            "meta": {
                "message": "查询数据成功",
                "status": "success",
            },
        }

    @jwt_required()
    @validate()
    def post(self, body: UserModel):
        user = UserORM()
        user.username = body.username
        user.nickname = body.nickname
        user.password = body.password
        user.mobile = body.mobile
        user.email = body.email
        user.gender = body.gender
        user.education = body.education

        role_ids: str = request.json.get("role_ids")
        role_ids_arr = role_ids.split(",")
        roles = RoleORM.query.filter(RoleORM.id.in_(role_ids_arr)).all()
        user.role = []
        user.role = roles

        db.session.add(user)
        db.session.commit()
        return {
            "meta": {
                "message": "添加数据成功",
                "status": "success",
            },
        }

    @jwt_required()
    @validate()
    def put(self, uid, body: UserModel):
        user = UserORM.query.get(uid)
        user.username = body.username
        user.nickname = body.nickname
        if body.password:
            user.password = body.password
        user.mobile = body.mobile
        user.email = body.email
        user.gender = body.gender
        user.education = body.education
        user.state = body.state
        db.session.add(user)
        db.session.commit()

        role_ids: str = request.json.get("role_ids")
        role_ids_arr = role_ids.split(",")
        roles = RoleORM.query.filter(RoleORM.id.in_(role_ids_arr)).all()
        user.role = []
        user.role = roles
        db.session.commit()
        return {
            "meta": {
                "message": "修改数据成功",
                "status": "success",
            },
        }

    @jwt_required()
    def delete(self, uid):
        if uid in [1, 2, 3]:
            return {
                "meta": {
                    "message": "测试数据禁止删除",
                    "status": "fail",
                },
            }
        user = UserORM.query.get(uid)
        db.session.delete(user)
        db.session.commit()
        return {
            "meta": {
                "message": "删除数据成功",
                "status": "success",
            },
        }


class DepartmentApi(MethodView):
    class PaginationModel(BaseModel):
        query: str = Field(default="")
        page: int = Field(default=1)
        pre_page: int = Field(default=10)

    class DepartmentModel(BaseModel):
        address: t.Optional[str]
        name: t.Optional[str]
        email: t.Optional[str]
        leader: t.Optional[str]
        pid: t.Optional[int]
        phone: t.Optional[str]
        sort: t.Optional[int]
        enable: t.Optional[bool]

    @validate()
    def get(self, did, query: PaginationModel):
        if did:
            dept = DepartmentORM.query.filter_by(id=did).first()
            dept_data = {
                "id": dept.id,
                "name": dept.name,
                "leader": dept.leader,
                "email": dept.email,
                "phone": dept.phone,
                "status": dept.status,
                "sort": dept.sort,
                "address": dept.address,
            }
            return dict(success=True, message="ok", dept=dept_data)
        else:
            department_list: List[DepartmentORM] = DepartmentORM.query.all()

            action = request.args.get("action")
            if action == "tree":
                return {
                    "status": {"code": 200, "message": "默认"},
                    "data": [
                        {
                            "id": department.id,
                            "pid": department.pid,
                            "name": department.name,
                            "sort": department.sort,
                            "leader": department.leader,
                            "phone": department.phone,
                            "email": department.email,
                            "enable": department.enable,
                        }
                        for department in department_list
                    ],
                }

            return {
                "result": {
                    "department_list": [
                        {
                            "id": department.id,
                            "pid": department.pid,
                            "name": department.name,
                            "sort": department.sort,
                            "leader": department.leader,
                            "phone": department.phone,
                            "email": department.email,
                            "enable": department.enable,
                        }
                        for department in department_list
                    ],
                },
                "meta": {
                    "message": "查询数据成功",
                    "status": "success",
                },
            }

    @validate()
    def post(self, body: DepartmentModel):
        department = DepartmentORM(
            pid=body.pid,
            name=body.name,
            sort=body.sort,
            leader=body.leader,
            phone=body.phone,
            email=body.email,
            enable=body.enable,
            address=body.address,
        )
        db.session.add(department)
        db.session.commit()

        return {
            "meta": {
                "message": "新增部门数据成功",
                "status": "success",
            },
        }

    @validate()
    def put(self, did, body: DepartmentModel):
        department_data = {
            "pid": body.pid,
            "name": body.name,
            "sort": body.sort,
            "leader": body.leader,
            "phone": body.phone,
            "email": body.email,
            "enable": body.enable,
            "address": body.address,
        }
        ret = DepartmentORM.query.filter_by(id=did).update(department_data)
        db.session.commit()
        return {
            "meta": {
                "message": "更新部门数据成功",
                "status": "success",
            },
        }

    def delete(self, did):
        ret = DepartmentORM.query.filter_by(id=did).delete()
        UserORM.query.filter(UserORM.department_id == did).update(
            {"department_id": None}
        )
        db.session.commit()
        if ret:
            return {
                "meta": {
                    "message": "删除部门数据成功",
                    "status": "success",
                },
            }
        return {
            "meta": {
                "message": "删除部门数据失败",
                "status": "fail",
            },
        }


def user_role(uid):
    roles: List[RoleORM] = RoleORM.query.all()
    if request.method == "GET":
        user: UserORM = UserORM.query.get(uid)
        rets = []
        for role in roles:
            if role in user.role:
                rets.append(
                    {
                        "id": role.id,
                        "name": role.name,
                        "desc": role.desc,
                    }
                )
        return {
            "result": {
                "user_role": rets,
            },
            "meta": {
                "message": "查询数据成功",
                "status": "success",
            },
        }
