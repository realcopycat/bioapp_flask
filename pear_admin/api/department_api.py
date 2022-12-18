# -*- coding: utf-8 -*-
from flask import request
from flask.views import MethodView
from flask_pydantic import validate

from pear_admin.models import DepartmentModel, PaginationModel
from pear_admin.orms import DepartmentORM


class DepartmentApi(MethodView):
    @validate()
    def get(self, did, query: PaginationModel):
        if did:
            dept: DepartmentORM = DepartmentORM.find_by_id(did)
            return dict(success=True, message="ok", dept=dept.json())
        else:
            department_list: list[DepartmentORM] = DepartmentORM.query.all()

            action = request.args.get("action")
            if action == "tree":
                return {
                    "status": {"code": 200, "message": "默认"},
                    "data": [department.json() for department in department_list],
                }

            return {
                "result": {
                    "department_list": [
                        department.json() for department in department_list
                    ],
                },
                "meta": {
                    "message": "查询数据成功",
                    "status": "success",
                },
            }

    @validate()
    def post(self, body: DepartmentModel):
        department = DepartmentORM()
        department.pid = (body.pid,)
        department.name = (body.name,)
        department.sort = (body.sort,)
        department.leader = (body.leader,)
        department.phone = (body.phone,)
        department.email = (body.email,)
        department.enable = (body.enable,)
        department.address = (body.address,)
        department.save_to_db()

        return {
            "meta": {
                "message": "新增部门数据成功",
                "status": "success",
            },
        }

    @validate()
    def put(self, did, body: DepartmentModel):
        department: DepartmentORM = DepartmentORM.find_by_id(did)
        department.pid = body.pid
        department.name = body.name
        department.sort = body.sort
        department.leader = body.leader
        department.phone = body.phone
        department.email = body.email
        department.enable = body.enable
        department.address = body.address
        department.save_to_db()
        return {
            "meta": {
                "message": "更新部门数据成功",
                "status": "success",
            },
        }

    def delete(self, did):
        ret: DepartmentORM = DepartmentORM.find_by_id(did)
        ret.delete_from_db()
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


def batch_remove_api():
    ids = request.json.get("ids")
    id_list = ids.split(",")
    for did in id_list:
        DepartmentORM.delete_by_id(did)
    return {
        "meta": {
            "message": "批量删除数据成功",
            "status": "success",
        },
    }
