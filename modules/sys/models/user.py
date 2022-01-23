from common.BaseModel import BaseBaseModel, Column, String, Integer
from pydantic import BaseBaseModel as PBaseModel


class User(BaseBaseModel):
    __tablename__ = 'admin_user'
    id = Column(Integer, primary_key=True, autoincrement=True, comment='用户ID')
    username = Column(String(20), comment='用户名')


class Test(BaseBaseModel):
    __tablename__ = 'admin_test'
    id = Column(Integer, primary_key=True, autoincrement=True, comment='ID')
    name = Column(String(20), comment='名')


class Userschema(PBaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
