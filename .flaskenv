# flask配置
FLASK_APP = app.py
FLASK_ENV = production
FLASK_DEBUG = 1
FLASK_RUN_HOST = 0.0.0.0
FLASK_RUN_PORT = 5000

# pear admin flask配置
SYSTEM_NAME = Pear Admin

# MySql配置信息
MYSQL_HOST = 127.0.0.1
# MYSQL_HOST = dbserver
MYSQL_PORT = 3306
MYSQL_DATABASE = pearadmin
MYSQL_USERNAME = root
MYSQL_PASSWORD = root

# Redis 配置
# REDIS_HOST = 127.0.0.1
# REDIS_PORT = 6379

# 密钥配置(记得改)
SECRET_KEY = pear-admin-flask

# 邮箱配置
MAIL_SERVER = xx.com
MAIL_USERNAME = xx@xx.com
MAIL_PASSWORD = xxx # 生成的授权码

# 插件配置 json 格式，填入插件的文件夹名
PLUGIN_ENABLE_FOLDERS = ["helloworld"]