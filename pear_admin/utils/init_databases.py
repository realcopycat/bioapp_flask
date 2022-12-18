import json
import os

from config import root_path
from pear_admin import DepartmentORM, PermissionORM, RoleORM, UserORM, db


def update_orm(obj, data):
    for key, value in data.items():
        setattr(obj, key, value)


def init_databases():
    db.drop_all()
    db.create_all()

    init_department()
    init_permission()
    init_role()
    init_role_permission()
    init_user()
    init_user_role()


def init_department():
    file_path = os.path.join("static", "data", "department.json")
    full_file_path = os.path.join(root_path, file_path)
    data = open(full_file_path, encoding="utf-8").read()
    department_list = json.loads(data)
    for department in department_list:
        department_obj = DepartmentORM()
        update_orm(department_obj, department)
        db.session.add(department_obj)
    db.session.commit()


def init_permission():
    file_path = os.path.join("static", "data", "permission.json")
    full_file_path = os.path.join(root_path, file_path)
    data = open(full_file_path, encoding="utf-8").read()
    permission_list = json.loads(data)
    for permission in permission_list:
        permission_obj = PermissionORM()
        update_orm(permission_obj, permission)
        db.session.add(permission_obj)
    db.session.commit()


def init_role():
    file_path = os.path.join("static", "data", "role.json")
    full_file_path = os.path.join(root_path, file_path)
    data = open(full_file_path, encoding="utf-8").read()
    role_list = json.loads(data)
    for role in role_list:
        role_obj = RoleORM()
        update_orm(role_obj, role)
        db.session.add(role_obj)
    db.session.commit()


def init_role_permission():
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


def init_user():
    file_path = os.path.join("static", "data", "user.json")
    full_file_path = os.path.join(root_path, file_path)
    data = open(full_file_path, encoding="utf-8").read()
    user_list = json.loads(data)
    for user in user_list:
        user_obj = UserORM()
        for key, value in user.items():
            if key == "password":
                user_obj.password = value
            else:
                setattr(user_obj, key, value)
        db.session.add(user_obj)
    db.session.commit()


def init_user_role():
    user_role_items = {
        1: [1],
        2: [2],
        3: [3],
    }
    for user_id, role_ids in user_role_items.items():
        user: UserORM = UserORM.query.get(user_id)
        role_list: [RoleORM] = RoleORM.query.filter(RoleORM.id.in_(role_ids)).all()
        user.role = role_list
    db.session.commit()
