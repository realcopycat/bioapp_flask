from common.model import Table, Column, Integer, ForeignKey

user_role = Table(
    "admin_user_role",
    Column("id", Integer, primary_key=True, autoincrement=True, comment='标识'),
    Column("user_id", Integer, ForeignKey("admin_user.id"), comment='用户编号'),
    Column("role_id", Integer, ForeignKey("admin_role.id"), comment='角色编号'),
)
