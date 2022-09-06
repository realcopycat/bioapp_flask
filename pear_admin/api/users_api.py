# -*- coding: utf-8 -*-
from typing import List

from flask.views import MethodView
from flask_pydantic import validate
from flask_sqlalchemy import Pagination
from pydantic import BaseModel, Field

from pear_admin.extensions import db
from pear_admin.models import UserORM


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
        db.session.add(user)
        db.session.commit()
        return {
            "meta": {
                "message": "添加数据成功",
                "status": "success",
            },
        }

    @validate()
    def put(self, uid, body: UserModel):
        user = UserORM.query.get(uid)
        user.username = body.username
        user.nickname = body.nickname
        if body.username:
            user.password = body.password
        user.mobile = body.mobile
        user.email = body.email
        user.gender = body.gender
        user.education = body.education
        user.state = body.state
        db.session.add(user)
        db.session.commit()
        return {
            "meta": {
                "message": "修改数据成功",
                "status": "success",
            },
        }

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
