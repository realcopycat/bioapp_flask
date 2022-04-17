from flask import Flask
from flask_limiter import Limiter
from flask import request


def limit_key_func():
    return str(request.headers.get("X-Forwarded-For", '127.0.0.1'))


def init_limiter(app: Flask):
    limiter = Limiter(
        app,
        key_func=limit_key_func,
        # 每天200次，一小时50次
        default_limits=["200 per day", "50 per hour"]
    )
