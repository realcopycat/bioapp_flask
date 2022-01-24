import datetime

from common.model import BaseModel, Integer, Column, String, CHAR, DateTime, SQLAlchemyAutoSchema


class File(BaseModel):
    __tablename__ = 'sys_file'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    href = Column(String(255))
    mime = Column(CHAR(50), nullable=False)
    size = Column(CHAR(30), nullable=False)
    create_time = Column(DateTime, default=datetime.datetime.now)


class AdminLogSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = False
        include_fk = True
        load_instance = True
