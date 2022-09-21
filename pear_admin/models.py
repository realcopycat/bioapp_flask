# -*- coding: utf-8 -*-
from datetime import datetime

from werkzeug.security import check_password_hash, generate_password_hash

from pear_admin.extensions import db

user_role = db.Table(
    "ums_user_role",  # 中间表名称
    db.Column("id", db.Integer, primary_key=True, autoincrement=True, comment="标识"),
    db.Column("user_id", db.Integer, db.ForeignKey("ums_user.id"), comment="用户编号"),
    db.Column("role_id", db.Integer, db.ForeignKey("ums_role.id"), comment="角色编号"),
)

role_permission = db.Table(
    "ums_role_permission",  # 中间表名称
    db.Column("id", db.Integer, primary_key=True, autoincrement=True, comment="标识"),
    db.Column(
        "permission_id", db.Integer, db.ForeignKey("ums_permission.id"), comment="用户编号"
    ),
    db.Column("role_id", db.Integer, db.ForeignKey("ums_role.id"), comment="角色编号"),
)


class UserORM(db.Model):
    __tablename__ = "ums_user"

    id = db.Column(db.Integer, primary_key=True, comment="自增id")
    username = db.Column(db.String(128), nullable=False, comment="登录名")
    nickname = db.Column(db.String(128), nullable=False, comment="昵称")
    password_hash = db.Column(db.String(102), nullable=False, comment="登录密码")
    mobile = db.Column(db.String(32), nullable=False, comment="手机")
    email = db.Column(db.String(64), nullable=False, comment="邮箱")
    gender = db.Column(
        db.Enum("保密", "女", "男"),
        nullable=False,
        default="女",
        comment="性别",
    )
    education = db.Column(
        db.Enum("博士", "硕士", "本科", "专科", "高中", "初中", "小学"),
        nullable=False,
        default="专科",
        comment="学历",
    )
    state = db.Column(db.Boolean, default=False, comment="用户状态 False 停止使用，True 正常使用")
    introduce = db.Column(db.Text, comment="简介")
    avatar = db.Column(db.Text, comment="头像地址")
    create_at = db.Column(
        db.Integer,
        nullable=False,
        comment="创建时间",
        default=datetime.now().timestamp,
    )

    role = db.relationship(
        "RoleORM",
        secondary="ums_user_role",
        backref=db.backref("user"),
        lazy="dynamic",
    )

    department_id = db.Column(
        db.Integer, db.ForeignKey("ums_department.id"), default=1, comment="部门id"
    )

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password=password)


class RoleORM(db.Model):
    __tablename__ = "ums_role"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, comment="角色名称")
    desc = db.Column(db.Text)

    permission_ids = db.Column(
        db.String(512),
        comment="权限ids,1,2,5。冗余字段，用户缓存用户权限",
    )

    permission = db.relationship(
        "PermissionORM", secondary="ums_role_permission", backref=db.backref("role")
    )


class PermissionORM(db.Model):
    __tablename__ = "ums_permission"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, comment="权限名称")
    level = db.Column(
        db.Integer,
        nullable=False,
        default=0,
        comment="权限等级",
    )
    code = db.Column(db.String(30), comment="权限标识")
    icon = db.Column(db.String(128), comment="图标")
    path = db.Column(db.String(30), comment="访问路径")
    open_type = db.Column(db.String(30), comment="打开方式")
    enable = db.Column(db.Boolean, comment="是否开启", default=True)
    sort = db.Column(db.Integer, comment="排序", default=0)

    pid = db.Column(db.Integer, db.ForeignKey("ums_permission.id"), comment="父类编号")
    parent = db.relationship("PermissionORM", remote_side=[id])  # 自关联


class DepartmentORM(db.Model):
    __tablename__ = "ums_department"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), comment="部门名称")
    leader = db.Column(db.String(50), comment="负责人")
    phone = db.Column(db.String(20), comment="联系方式")
    address = db.Column(db.String(255), comment="详细地址")

    users = db.relationship("UserORM", backref="department")

    pid = db.Column(db.Integer, db.ForeignKey("ums_department.id"))
    parent = db.relationship("DepartmentORM", remote_side=[id], backref="child")  # 自关联
