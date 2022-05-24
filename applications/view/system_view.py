from flask import Blueprint, render_template

system_bp = Blueprint('system', __name__)


@system_bp.route('/view/system/user.html')
def system_user():
    return render_template('view/system/user.html')


@system_bp.route('/view/system/role.html')
def system_role():
    return render_template('view/system/role.html')


@system_bp.route('/view/system/power.html')
def system_power():
    return render_template('view/system/power.html')


@system_bp.route('/view/system/department.html')
def system_department():
    return render_template('view/system/department.html')


@system_bp.route('/view/system/log.html')
def system_log():
    return render_template('view/system/log.html')


@system_bp.route('/view/system/dict.html')
def system_dict():
    return render_template('view/system/dict.html')


@system_bp.route('/view/system/operate/add.html')
def system_operate_add():
    return render_template('view/system/operate/add.html')


@system_bp.route('/view/system/operate/edit.html')
def system_operate_edit():
    return render_template('view/system/operate/edit.html')


@system_bp.route('/view/system/operate/profile.html')
def system_operate_profile():
    return render_template('view/system/operate/profile.html')
