from flask import request, jsonify
from flask.views import MethodView
from flask_login import current_user
from flask_restful import reqparse
from sqlalchemy import desc

from common.utils.http import fail_api, success_api, table_api
from extensions import db
from models import UserModel, RoleModel, DepartmentModel
from models import LogModel


def get_current_user_logs():
    """ 获取当前用户日志 """
    log = LogModel.query.filter_by(url='/passport/login').filter_by(uid=current_user.id).order_by(
        desc(LogModel.create_at)).limit(10)
    return log


def is_user_exists(username):
    """ 判断用户是否存在 """
    res = UserModel.query.filter_by(username=username).count()
    return bool(res)


def delete_by_id(_id):
    """ 删除用户 """
    user = UserModel.query.filter_by(id=_id).first()
    roles_id = []
    for role in user.role:
        roles_id.append(role.id)
    roles = RoleModel.query.filter(RoleModel.id.in_(roles_id)).all()
    for r in roles:
        user.role.remove(r)
    res = UserModel.query.filter_by(id=_id).delete()
    db.session.commit()
    return res


def batch_remove(ids):
    """ 批量删除 """
    for _id in ids:
        delete_by_id(_id)


def update_user_role(_id, roles_list):
    user = UserModel.query.filter_by(id=_id).first()
    roles_id = []
    for role in user.role:
        roles_id.append(role.id)
    roles = RoleModel.query.filter(RoleModel.id.in_(roles_id)).all()
    for r in roles:
        user.role.remove(r)
    roles = RoleModel.query.filter(RoleModel.id.in_(roles_list)).all()
    for r in roles:
        user.role.append(r)
    db.session.commit()


def users_delete():
    """批量删除"""
    ids = request.form.getlist('ids[]')
    batch_remove(ids)
    return success_api(message="批量删除成功")


class UserApi(MethodView):
    """修改用户数据"""

    def get(self, _id):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, default=1)
        parser.add_argument('limit', type=int, default=10)
        parser.add_argument('realName', type=str, dest='real_name')
        parser.add_argument('username', type=str)
        parser.add_argument('deptId', type=int, dest='dept_id', default=0)

        res = parser.parse_args()

        filters = []

        if res.real_name:
            filters.append(UserModel.realname.like('%' + res.real_name + '%'))
        if res.username:
            filters.append(UserModel.username.like('%' + res.username + '%'))
        if res.dept_id:
            filters.append(UserModel.dept_id == res.dept_id)

        paginate = UserModel.query.filter(*filters).paginate(page=res.page,
                                                             per_page=res.limit,
                                                             error_out=False)

        dept_name = lambda dept_id: DepartmentModel.query.filter_by(id=dept_id).first().dept_name if dept_id else ""
        user_data = [{
            'id': item.id,
            'username': item.username,
            'realname': item.realname,
            'enable': item.enable,
            'create_at': str(item.create_at),
            'update_at': str(item.update_at),
            'dept': dept_name(item.dept_id),
        } for item in paginate.items]
        return table_api(result={'items': user_data,
                                 'total': paginate.total}
                         , code=0)

    def post(self):
        """新建单个用户"""
        parser = reqparse.RequestParser()
        parser.add_argument("roleIds", type=str, dest='role_ids')
        parser.add_argument("username", type=str, required=True, help="用户名不能为空")
        parser.add_argument("realName", type=str, required=True, help="真实姓名不能为空", dest='real_name')
        parser.add_argument("password", type=str, required=True, help="密码不得为空")

        res = parser.parse_args()

        role_ids = res.role_ids.split(',')

        if is_user_exists(res.username):
            return fail_api(message="用户已经存在")

        user = UserModel()
        user.username = res.username
        user.realname = res.real_name
        user.set_password(res.password)
        db.session.add(user)
        db.session.commit()

        """ 增加用户角色 """
        user = UserModel.query.filter_by(id=user.id).first()
        roles = RoleModel.query.filter(RoleModel.id.in_(role_ids)).all()
        for r in roles:
            user.role.append(r)
        db.session.commit()

        return success_api(message="增加成功", code=0)

    def delete(self, _id):
        # 删除用户
        res = delete_by_id(_id)
        if not res:
            return fail_api(message="删除失败")
        return success_api(message="删除成功")


def user_role_resource(_id):
    parser = reqparse.RequestParser()
    parser.add_argument('roleIds', type=str, dest='role_ids')
    parser.add_argument('userId', type=str, dest='user_id')
    parser.add_argument('username', type=str)
    parser.add_argument('realName', type=str, dest='real_name')
    parser.add_argument('deptId', type=str, dest='dept_id')

    res = parser.parse_args()
    role_ids = res.role_ids.split(',')

    # 更新用户数据
    UserModel.query.filter_by(id=_id).update({'username': res.username,
                                              'realname': res.real_name,
                                              'dept_id': res.dept_id})
    db.session.commit()

    update_user_role(_id, role_ids)

    return success_api(message="更新成功")


def user_info(_id, action):
    if action == 'info':
        parser = reqparse.RequestParser()
        parser.add_argument('realName', type=str, dest='real_name')
        parser.add_argument('username', type=str)
        parser.add_argument('remark', type=str)
        parser.add_argument('details', type=str)

        res = parser.parse_args()

        ret = UserModel.query.get(_id)
        ret.username = res.username
        ret.realname = res.real_name
        ret.remark = res.details
        db.session.commit()
        if not ret:
            return fail_api(message="出错啦")
        return success_api(message="更新成功")
    elif action == 'status':
        parser = reqparse.RequestParser()
        parser.add_argument('userId', type=int, required=True, dest='user_id')
        parser.add_argument('operate', type=int, required=True, dest='operate', choices=[0, 1])

        res = parser.parse_args()

        if res.operate == 1:
            user = UserModel.query.get(_id)
            user.enable = res.operate
            message = success_api(message="启动成功")
        else:
            user = UserModel.query.filter_by(id=res.user_id).update({"enable": res.operate})
            message = success_api(message="禁用成功")
        if user:
            db.session.commit()
        else:
            return fail_api(message="出错啦")
        return message
    elif action == 'avatar':
        url = request.json.get("avatar").get("src")
        ret = UserModel.query.get(_id)
        ret.avatar = url
        db.session.commit()
        if not ret:
            return fail_api(message="出错啦")
        return success_api(message="修改成功")
    elif action == 'password':
        parser = reqparse.RequestParser()
        parser.add_argument('oldPassword', type=str, required=True, help='旧密码不得为空')
        parser.add_argument('newPassword', type=str, required=True, help='新密码不得为空')
        parser.add_argument('confirmPassword', type=str, required=True, help='确认密码不能为空')

        res = parser.parse_args()

        if res.newPassword != res.confirmPassword:
            return fail_api(message='确认密码不一致')

        """ 修改当前用户密码 """
        user = UserModel.query.get(_id)
        is_right = user.validate_password(res.oldPassword)
        if not is_right:
            return jsonify(success=False, message="旧密码错误")
        user.set_password(res.newPassword)
        db.session.add(user)
        db.session.commit()

        return jsonify(success=True, message="更改成功")
    else:
        return jsonify(success=False, message="操作有误")
