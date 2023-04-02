# -*- coding: utf-8 -*-
from pear_admin.extensions import db


class RightsORM(db.Model):
    __tablename__ = "ums_permission"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, comment="权限名称")
    code = db.Column(db.String(30), comment="权限标识")
    type = db.Column(db.String(30), comment="权限类型")
    url = db.Column(db.String(30), comment="路径地址")

    icon = db.Column(db.String(128), comment="图标")
    status = db.Column(db.Boolean, default=True, comment="是否开启")
    sort = db.Column(db.Integer, default=1)
    open_type = db.Column(db.String(128), comment="打开方式")
    pid = db.Column(
        db.Integer,
        db.ForeignKey("ums_permission.id"),
        default=0,
        comment="父类编号",
    )

    # parent = db.relationship("RightsORM", remote_side=[permission_id])  # 自关联

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "type": self.type,
            "url": self.url,
            "icon": self.icon,
            "status": self.status,
            "sort": self.sort,
            "open_type": self.open_type,
            "pid": self.pid,
        }

    def menu_json(self):
        type_map_dict = {"menu": 0, "path": 1}

        return {
            "id": self.id,
            "pid": self.pid,
            "permission_id": self.id,
            "title": self.name,
            "type": type_map_dict[self.type],
            "href": self.url,
            "icon": self.icon,
            "sort": self.sort,
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
