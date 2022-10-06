# -*- coding: utf-8 -*-
from pear_admin.extensions import db


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

    def json(self):
        return {
            "id": self.id,
            "pid": self.pid,
            "level": self.level,
            "name": self.name,
            "code": self.code,
            "icon": self.icon,
            "path": self.path,
            "open_type": self.open_type,
            "enable": self.enable,
            "sort": self.sort or 0,
        }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
