from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required

from applications.common.curd import model_to_dicts, enable_status, disable_status, get_one_by_id
from applications.common.utils.http import table_api, success_api, fail_api
from applications.common.utils.rights import authorize
from applications.common.utils.validate import str_escape
from sqlalchemy import func
from applications.extensions import db
from applications.models import Role, RoleGroup, Power, User
from applications.schemas import RoleOutSchema, PowerOutSchema2,RoleGroupSchema

bp = Blueprint('role', __name__, url_prefix='/role')

# 用户管理
@bp.get('/')
@authorize("system:role:main")
def main():
    return render_template('system/role/main.html')


# 表格数据
@bp.get('/data')
@authorize("system:role:main")
def table():
    role_name = str_escape(request.args.get('roleName', type=str))
    role_code = str_escape(request.args.get('roleCode', type=str))
    filters = []
    if role_name:
        filters.append(Role.name.contains(role_name))
    if role_code:
        filters.append(Role.code.contains(role_code))
    roles = Role.query.filter(*filters).layui_paginate()
    return table_api(data=RoleOutSchema(many=True).dump(roles), count=roles.total)


# 角色增加
@bp.get('/add')
@authorize("system:role:add", log=True)
def add():
    roleGroups=RoleGroup.query.order_by(RoleGroup.id.asc()).all()
    selectDic=[{"name":roleGroup.name,"value":roleGroup.id} for roleGroup in roleGroups]
    return render_template('system/role/add.html',selectDic=selectDic)


# 角色增加
@bp.post('/save')
@authorize("system:role:add", log=True)
def save():
    req = request.get_json(force=True)
    details = str_escape(req.get("details"))
    enable = str_escape(req.get("enable"))
    roleCode = str_escape(req.get("roleCode"))
    roleName = str_escape(req.get("roleName"))
    groupId = str_escape(req.get("groupId"))
    sort = str_escape(req.get("sort"))
    role = Role(
        details=details,
        enable=enable,
        code=roleCode,
        name=roleName,
        sort=sort,
        group_id=groupId
    )
    db.session.add(role)
    db.session.commit()
    return success_api(msg="成功")


# 角色授权
@bp.get('/power/<int:_id>')
@authorize("system:role:power", log=True)
def power(_id):
    return render_template('system/role/power.html', id=_id)


# 获取角色权限
@bp.get('/getRolePower/<int:id>')
@authorize("system:role:main", log=True)
def get_role_power(id):
    role = Role.query.filter_by(id=id).first()
    check_powers = role.power
    check_powers_list = []
    for cp in check_powers:
        check_powers_list.append(cp.id)
    powers = Power.query.all()
    power_schema = PowerOutSchema2(many=True)  # 用已继承ma.ModelSchema类的自定制类生成序列化类
    output = power_schema.dump(powers)  # 生成可序列化对象
    for i in output:
        if int(i.get("powerId")) in check_powers_list:
            i["checkArr"] = "1"
        else:
            i["checkArr"] = "0"
    res = {
        "data": output,
        "status": {"code": 200, "message": "默认"}
    }
    return jsonify(res)


# 保存角色权限
@bp.put('/saveRolePower')
@authorize("system:role:edit", log=True)
def save_role_power():
    req_form = request.form
    power_ids = req_form.get("powerIds")
    power_list = power_ids.split(',')
    role_id = req_form.get("roleId")
    role = Role.query.filter_by(id=role_id).first()

    powers = Power.query.filter(Power.id.in_(power_list)).all()
    role.power = powers

    db.session.commit()
    return success_api(msg="授权成功")


# 角色编辑
@bp.get('/edit/<int:id>')
@authorize("system:role:edit", log=True)
def edit(id):
    role = get_one_by_id(model=Role, id=id)
    roleGroups=RoleGroup.query.order_by(RoleGroup.id.asc()).all()
    selectDic=[{"name":roleGroup.name,"value":roleGroup.id} for roleGroup in roleGroups]
    return render_template('system/role/edit.html', role=role,selectDic=selectDic)


# 更新角色
@bp.put('/update')
@authorize("system:role:edit", log=True)
def update():
    req_json = request.get_json(force=True)
    id = req_json.get("roleId")
    data = {
        "code": str_escape(req_json.get("roleCode")),
        "name": str_escape(req_json.get("roleName")),
        "sort": str_escape(req_json.get("sort")),
        "enable": str_escape(req_json.get("enable")),
        "details": str_escape(req_json.get("details"))
    }
    role = Role.query.filter_by(id=id).update(data)
    db.session.commit()
    if not role:
        return fail_api(msg="更新角色失败")
    return success_api(msg="更新角色成功")


# 启用用户
@bp.put('/enable')
@authorize("system:role:edit", log=True)
def enable():
    id = request.get_json(force=True).get('roleId')
    if id:
        res = enable_status(Role, id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api(msg="启动成功")
    return fail_api(msg="数据错误")


# 禁用用户
@bp.put('/disable')
@authorize("system:role:edit", log=True)
def dis_enable():
    _id = request.get_json(force=True).get('roleId')
    if _id:
        res = disable_status(Role, _id)
        if not res:
            return fail_api(msg="出错啦")
        return success_api(msg="禁用成功")
    return fail_api(msg="数据错误")


# 角色删除
@bp.delete('/remove/<int:id>')
@authorize("system:role:remove", log=True)
def remove(id):
    role = Role.query.filter_by(id=id).first()
    # 删除该角色的权限和用户
    role.power = []
    role.user = []

    r = Role.query.filter_by(id=id).delete()
    db.session.commit()
    if not r:
        return fail_api(msg="角色删除失败")
    return success_api(msg="角色删除成功")


# 角色分组管理
@bp.get('/group')
@authorize("system:role:add", log=True)
def group():
    obj=RoleGroup.query.with_entities(func.max(RoleGroup.sort)).first()
    if obj:
        maxSort=obj[0]+1
    else:
        maxSort=1
    return render_template('system/role/group.html',sort=maxSort)

# 角色分组管理
@bp.get('/group/data')
@authorize("system:role:add", log=True)
def groupData():
    print("jaja")
    roleGroups = RoleGroup.query.order_by(RoleGroup.sort.asc()).layui_paginate()
    return table_api(data=RoleGroupSchema(many=True).dump(roleGroups), count=roleGroups.total)

# 角色分组编辑
@bp.put('/group/update')
@authorize("system:role:edit", log=True)
def groupUpdate():
    req_json = request.get_json(force=True)
    id = req_json.get("id")

    roleGroup=get_one_by_id(RoleGroup,id)

    if roleGroup.name=="默认分组":
        return fail_api(msg="默认分组不允许修改")
    data = {
        "name": str_escape(req_json.get("name")),
        "sort": str_escape(req_json.get("sort")),
        "remark": str_escape(req_json.get("remark"))
    }

    role = RoleGroup.query.filter_by(id=id).update(data)
    db.session.commit()
    if not role:
        return fail_api(msg="更新角色分组失败")
    return success_api(msg="更新角色分组成功")


# 角色分组增加
@bp.post('/group/save')
@authorize("system:role:add", log=True)
def groupSave():
    req = request.get_json(force=True)
    name = str_escape(req.get("name"))
    sort = str_escape(req.get("sort"))
    remark = str_escape(req.get("remark"))

    roleGroup = RoleGroup.query.filter_by(name="name").first()
    if roleGroup:
        return fail_api(msg="改分组名称已存在！")

    roleGroup = RoleGroup(
        name=name,
        sort=sort,
        remark=remark,
    )
    db.session.add(roleGroup)
    db.session.commit()
    return success_api(msg="成功")

# 角色分组删除
@bp.delete('/group/remove/<int:id>')
@authorize("system:role:remove", log=True)
def groupRemove(id):

    roleGroup = RoleGroup.query.filter_by(id=id).first()
    if roleGroup.name=="默认分组":
        return fail_api(msg="默认分组不能删除!")

    roleGroupDefault = RoleGroup.query.filter_by(name="默认分组").first()
    if len(roleGroup.roles)>0:
        roleGroupDefault.roles=roleGroupDefault.roles+roleGroup.roles
    r=RoleGroup.query.filter_by(id=id).delete()
    db.session.commit()
    if not r:
        return fail_api(msg="角色分组删除失败")
    return success_api(msg="角色分组删除成功")


