import datetime

from common.model import BaseModel, Column, Integer, String, Text, DateTime, SQLAlchemyAutoSchema


class AdminLog(BaseModel):
    __tablename__ = 'sys_admin_log'
    id = Column(Integer, primary_key=True)
    method = Column(String(10))
    uid = Column(Integer)
    url = Column(String(255))
    desc = Column(Text)
    ip = Column(String(255))
    success = Column(Integer)
    user_agent = Column(Text)
    create_time = Column(DateTime, default=datetime.datetime.now)


class AdminLogSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = AdminLog
        include_fk = True
        load_instance = True
