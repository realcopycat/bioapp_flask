from common.model import Column, Table, Integer, ForeignKey

role_power = Table(
    "sys_role_power",
    Column("id", Integer, primary_key=True, autoincrement=True, comment='标识'),
    Column("power_id", Integer, ForeignKey("sys_power.id"), comment='用户编号'),
    Column("role_id", Integer, ForeignKey("sys_role.id"), comment='角色编号'),
)
