
from modules.sys.models.user_role import user_role
from modules.sys.models.role_power import role_power
from modules.sys.models.dict import DictType, DictData
from modules.sys.models.admin_log import AdminLog
from modules.sys.models.photo import Photo
from modules.sys.models.power import Power
from modules.sys.models.role import Role
from modules.sys.models.dept import Dept

from modules.sys.models.user import User


model_lists: list = [
    role_power,
    user_role,
    Dept,
    DictType, DictData,
    AdminLog,
    Photo,
    Power,
    Role,
    User,

]
