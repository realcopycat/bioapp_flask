# -*- coding: utf-8 -*-
import logging

# 默认日志等级
LOG_LEVEL = logging.WARN

# mysql 配置
MYSQL_USERNAME = "root"
MYSQL_PASSWORD = "root"

MYSQL_HOST = "127.0.0.1"
MYSQL_PORT = 3306
MYSQL_DATABASE = "pear_admin_flask"
# mysql 数据库的配置信息
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# redis 配置
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379


JWT_SECRET_KEY = "pear_admin_flask_jwt_token"
JWT_TOKEN_LOCATION = ["headers", "cookies"]
