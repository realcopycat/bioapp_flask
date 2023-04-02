# -*- coding: utf-8 -*-
from datetime import datetime

from werkzeug.security import check_password_hash, generate_password_hash

from pear_admin.extensions import db


class UserORM(db.Model):
    __tablename__ = "ums_user"

    id = db.Column(db.Integer, primary_key=True, comment="自增id")
    nickname = db.Column(db.String(128), nullable=False, comment="昵称")
    username = db.Column(db.String(128), nullable=False, comment="登录名")
    password_hash = db.Column(db.String(102), nullable=False, comment="登录密码")
    mobile = db.Column(db.String(32), nullable=False, comment="手机")
    email = db.Column(db.String(64), nullable=False, comment="邮箱")
    avatar = db.Column(db.Text, comment="头像地址")
    create_at = db.Column(
        db.DateTime,
        nullable=False,
        comment="创建时间",
        default=datetime.now,
    )
    department_id = db.Column(
        db.Integer, db.ForeignKey("ums_department.id"), default=1, comment="部门id"
    )

    role_list = db.relationship(
        "RoleORM",
        secondary="ums_user_role",
        backref=db.backref("user"),
        lazy="dynamic",
    )

    def json(self):
        return {
            "id": self.id,
            "username": self.username,
            "nickname": self.nickname,
            "mobile": self.mobile,
            "email": self.email,
            "create_at": self.create_at,
        }

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password=password)

    @classmethod
    def find_by_nickname(cls, nickname):
        return cls.query.filter_by(nickname=nickname).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
