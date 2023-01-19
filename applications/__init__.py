import os
from applications.dev import *

from flask import Flask, request

from applications.common.script import init_script
from applications.extensions import init_plugs
from applications.view import init_view
from applications.configs import config

from logging.config import dictConfig

def get_user_ip(request):
    """获取用户真实IP 来自 @FacebookLibra"""
    if 'HTTP_X_FORWARDED_FOR' in request.headers:
        arr = request.headers['HTTP_X_FORWARDED_FOR'].strip().split(",")
        i = 0
        while i < len(arr):
            if arr[i].find("unknown") != -1:
                del arr[i]
            else:
                i += 1
        if len(arr) != 0:
            return arr[0].strip()
    elif 'HTTP_CLIENT_IP' in request.headers:
        return request.headers['HTTP_CLIENT_IP']
    elif 'REMOTE_ADDR' in request.headers:
        return request.headers['REMOTE_ADDR']
    elif 'X-Forwarded-For' in request.headers:
        return request.headers['X-Forwarded-For']
    return request.remote_addr

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


def create_app(config_name=None):

    app = Flask(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

    # 移除原有的输出日志
    app.logger = None
    
    # 更改IP地址，只有在最新版的flask中才能生效
    @app.before_request
    def before_request():
        request.remote_addr = get_user_ip(request)
        
    
    # 使用自定义的日志输出
    @app.after_request
    def after_request(rep):
        if rep.status_code == 200:
            console.success(f"{request.remote_addr} -- {request.full_path} 200")
        elif rep.status_code == 404:
            console.error(f"{request.remote_addr} -- {request.full_path} 404")
        elif rep.status_code == 500:
            console.warning(f"{request.remote_addr} -- {request.full_path} 500")
        else:
            console.info(f"{request.remote_addr} -- {request.full_path} {rep.status_code}")
        return rep
    
    if not config_name:
        # 尝试从本地环境中读取
        config_name = os.getenv('FLASK_CONFIG', 'development')

    # 引入数据库配置
    app.config.from_object(config[config_name])

    # 注册各种插件
    init_plugs(app)

    # 注册路由
    init_view(app)

    # 注册命令
    init_script(app)

    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        logo()

    return app


def logo():
    print('''
 _____                              _           _         ______ _           _    
|  __ \                    /\      | |         (_)       |  ____| |         | |   
| |__) |__  __ _ _ __     /  \   __| |_ __ ___  _ _ __   | |__  | | __ _ ___| | __
|  ___/ _ \/ _` | '__|   / /\ \ / _` | '_ ` _ \| | '_ \  |  __| | |/ _` / __| |/ /
| |  |  __/ (_| | |     / ____ \ (_| | | | | | | | | | | | |    | | (_| \__ \   < 
|_|   \___|\__,_|_|    /_/    \_\__,_|_| |_| |_|_|_| |_| |_|    |_|\__,_|___/_|\_\\

    ''')
