# -*- coding: utf-8 -*-
from datetime import datetime

from flask import current_app
from werkzeug.security import check_password_hash, generate_password_hash

from pear_admin.extensions import db
from pear_admin.utils.response_code import RetCode


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
    state = db.Column(db.Boolean, default=False, comment="用户状态 False 停止使用，True 正常使用")
    introduce = db.Column(db.Text, comment="简介")
    avatar = db.Column(db.Text, comment="头像地址")
    create_at = db.Column(
        db.DateTime,
        nullable=False,
        comment="创建时间",
        default=datetime.now,
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

    def json(self):
        return {
            "id": self.id,
            "username": self.username,
            "nickname": self.nickname,
            "gender": self.gender,
            "mobile": self.mobile,
            "email": self.email,
            "state": self.state,
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
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        try:
            db.session.commit()
        except Exception as e:
            # 添加log
            current_app.logger.error(e)
            # 滚回操作
            db.session.rollback()
            return {
                "meta": {
                    "code": RetCode.DB_ERR.value,
                    "message": "添加数据成功",
                    "status": "fail",
                },
            }

    def delete_from_db(self):
        db.session.delete(self)
        try:
            db.session.commit()
        except Exception as e:
            # 添加log
            current_app.logger.error(e)
            # 滚回操作
            db.session.rollback()
            return {
                "meta": {
                    "code": RetCode.DB_ERR.value,
                    "message": "添加数据成功",
                    "status": "fail",
                },
            }
