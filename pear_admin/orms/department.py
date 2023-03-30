# -*- coding: utf-8 -*-
from flask import current_app

from pear_admin.extensions import db
from pear_admin.utils.response_code import RetCode


class DepartmentORM(db.Model):
    __tablename__ = "ums_department"
    id = db.Column(db.Integer, primary_key=True, comment="部门ID")
    name = db.Column(db.String(50), comment="部门名称")
    leader = db.Column(db.String(50), comment="负责人")
    phone = db.Column(db.String(20), comment="联系方式")
    email = db.Column(db.String(50), comment="邮箱")
    enable = db.Column(db.Boolean, comment="状态(1开启,0关闭)")
    comment = db.Column(db.Text, comment="备注")
    address = db.Column(db.String(255), comment="详细地址")
    sort = db.Column(db.Integer, comment="排序")

    users = db.relationship("UserORM", backref="department")

    pid = db.Column(db.Integer, db.ForeignKey("ums_department.id"))
    parent = db.relationship("DepartmentORM", remote_side=[id], backref="child")  # 自关联

    def json(self):
        return {
            "id": self.id,
            "pid": self.pid,
            "name": self.name,
            "leader": self.leader,
            "email": self.email,
            "phone": self.phone,
            "sort": self.sort,
            "enable": self.enable,
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
                    "message": "提交失败",
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
                    "message": "提交失败",
                    "status": "fail",
                },
            }

    @classmethod
    def delete_by_id(cls, did):
        dpm = cls.find_by_id(did)
        if not dpm:
            return {
                "meta": {
                    "code": RetCode.NODATA_ERR.value,
                    "message": "无数据",
                    "status": "fail",
                },
            }
        dpm.delete_from_db()
