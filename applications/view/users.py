from flask import render_template

from common.utils.rights import permission_required, view_logging_required
from models import RoleModel, UserModel
from . import index_bp


@index_bp.get('/users/add')
@view_logging_required
@permission_required("admin:user:add")
def users_add_view():
    roles = RoleModel.query.all()
    return render_template('view/system/user_add.html', roles=roles)


@index_bp.get('/users/<user_id>')
@view_logging_required
@permission_required("admin:user:edit")
def users_user_id_view(user_id):
    #  获取编辑用户信息
    user = UserModel.query.filter_by(id=user_id).first()
    roles = RoleModel.query.all()
    checked_roles = []
    for r in user.role:
        checked_roles.append(r.id)
    return render_template('view/system/user_edit.html', user=user, roles=roles, checked_roles=checked_roles)
