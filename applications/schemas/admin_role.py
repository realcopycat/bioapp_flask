from flask_marshmallow.sqla import SQLAlchemyAutoSchema
from applications.extensions import ma
from applications.extensions.init_sqlalchemy import db
from marshmallow import fields
from applications.models import Role


# class RoleOutSchema(SQLAlchemyAutoSchema):
    # class Meta:
    #     model = Role  # table = models.Album.__table__
    #     include_relationships = True  # 输出模型对象时同时对外键，是否也一并进行处理
    #     include_fk = True  # 序列化阶段是否也一并返回主键
    #     sqla_session=db.session
    #     # fields= ["id","name"] # 启动的字段列表
    #     # exclude = ["id","name"] # 排除字段列表

class RoleOutSchema(ma.Schema):
    id = fields.Integer()
    name = fields.Str()
    code = fields.Str()
    enable=fields.Integer()
    remark = fields.Str()
    details = fields.Str()
    sort = fields.Integer()
    create_time = fields.DateTime()
    update_time = fields.DateTime()
    group=fields.Nested(lambda:RoleGroupSchema())

# 用户models的序列化类
class RoleGroupSchema(ma.Schema):
    id = fields.Integer()
    name = fields.Str()
    remark = fields.Str()
    sort = fields.Integer()
    create_time = fields.DateTime()
    update_time = fields.DateTime()
    # roles = fields.Nested(lambda: RoleOutSchema())
