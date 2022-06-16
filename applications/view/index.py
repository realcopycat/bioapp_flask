from flask import Blueprint, redirect, url_for
from flask import send_file
from flask import session, render_template
from flask_login import current_user, logout_user, login_required

from common.gen_captcha import get_captcha_image

index_bp = Blueprint('index', __name__)


@index_bp.route('/')
@index_bp.route('/admin')
@login_required
def index():
    return render_template('index.html')


@index_bp.route('/config/pear.config.json')
def pear_config():
    return send_file('static/config/pear.config.json')


@index_bp.route('/admin/data/menu.json')
def menu():
    return send_file('static/admin/data/menu.json')


@index_bp.route('/admin/data/message.json')
def message():
    return send_file('static/admin/data/message.json')


@index_bp.route('/view/console/console1.html')
def console1():
    # 控制后台
    return render_template('view/console/console1.html')


@index_bp.route('/view/console/console2.html')
def console2():
    # 数据分析
    return render_template('view/console/console2.html')


@index_bp.route('/view/system/theme.html')
def theme():
    # 酸爽翻倍
    return render_template('view/system/theme.html')


@index_bp.route('/view/document/core.html')
def core():
    # 酸爽翻倍
    return render_template('view/document/core.html')


@index_bp.get('/passport/getCaptcha')
def get_captcha():
    resp, code = get_captcha_image()
    session["code"] = code
    return resp


# 退出登录
@index_bp.post('/logout')
@login_required
def logout():
    logout_user()
    session.pop('permissions')
    print({"message": "注销成功", "success": True})
    return {"message": "注销成功", "success": True}


@index_bp.get('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.index'))
    return render_template('login.html')
