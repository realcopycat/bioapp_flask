from common.model import BaseModel, Column, String, Integer
from pydantic import BaseModel as PModel


class User(BaseModel):
    __tablename__ = 'admin_user'
    id = Column(Integer, primary_key=True, autoincrement=True, comment='用户ID')
    username = Column(String(20), comment='用户名')


class Userschema(PModel):
    id: int
    username: str
    class Config:
        orm_mode = True
