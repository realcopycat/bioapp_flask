import datetime

from common.model import BaseModel, Column, Integer, String, Text, DateTime


class Dept(BaseModel):
    __tablename__ = 'sys_dept'
    id = Column(Integer, primary_key=True, comment="部门ID")
    parent_id = Column(Integer, comment="父级编号")
    dept_name = Column(String(50), comment="部门名称")
    sort = Column(Integer, comment="排序")
    leader = Column(String(50), comment="负责人")
    phone = Column(String(20), comment="联系方式")
    email = Column(String(50), comment="邮箱")
    status = Column(Integer, comment='状态(1开启,0关闭)')
    remark = Column(Text, comment="备注")
    address = Column(String(255), comment="详细地址")
    create_at = Column(DateTime, default=datetime.datetime.now, comment='创建时间')
    update_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment='创建时间')