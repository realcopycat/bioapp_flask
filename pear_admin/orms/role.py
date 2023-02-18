# -*- coding: utf-8 -*-
from datetime import datetime

from flask import current_app

from pear_admin.extensions import db
from pear_admin.utils.response_code import RetCode


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

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "desc": self.desc,
            "permission_ids": self.permission_ids,
        }

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

