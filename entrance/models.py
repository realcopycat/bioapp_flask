from modules.sys.models.admin_dept import Dept
from modules.sys.models.admin_dict import DictType, DictData
from modules.sys.models.admin_log import AdminLog
from modules.sys.models.admin_photo import Photo
from modules.sys.models.admin_power import Power
from modules.sys.models.admin_role import Role
from modules.sys.models.admin_role_power import role_power
from modules.sys.models.admin_user import User
from modules.sys.models.admin_user_role import user_role

model_lists: list = [
    Dept,
    DictType, DictData,
    AdminLog,
    Photo,
    Power,
    Role,
    role_power,
    User,
    user_role
]
