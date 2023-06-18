import logging
from urllib.parse import quote_plus as urlquote
from datetime import timedelta

class BaseConfig:
    SUPERADMIN = 'admin'

    SYSTEM_NAME = 'hml admin'
    # 主题面板的链接列表配置
    SYSTEM_PANEL_LINKS = [
        {
            "icon": "layui-icon layui-icon-auz",
            "title": "官方网站",
            "href": "/"
        },
        {
            "icon": "layui-icon layui-icon-auz",
            "title": "开发文档",
            "href": "/"
        },
        {
            "icon": "layui-icon layui-icon-auz",
            "title": "开源地址",
            "href": "/"
        }
    ]

    UPLOADED_PHOTOS_DEST = 'static/upload'
    UPLOADED_FILES_ALLOW = ['gif', 'jpg']
    UPLOADS_AUTOSERVE = True

    # JSON配置
    JSON_AS_ASCII = False

    SECRET_KEY = "hml-session-sec-key" # session用的是这个key #等替换了cache之后再删除
    JWT_SECRET_KEY = "hml-session-sec-key"
    # JWT_TOKEN_EXPIRATION=60 #60=1min
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=60)  # 设置默认的过期时间
    

    # mysql 配置
    MYSQL_USERNAME = "root"
    MYSQL_PASSWORD = "Brr0qZo6uo#6"
    MYSQL_HOST = "121.5.62.78"
    MYSQL_PORT = 3306
    MYSQL_DATABASE = "PearAdminFlask"

    # mysql 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USERNAME}:{urlquote(MYSQL_PASSWORD)}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4"

    # 下面五个参数是所有的类型共有的
    CACHE_NO_NULL_WARNING = "warning" # null类型时的警告消息
    CACHE_ARGS = []    # 在缓存类实例化过程中解包和传递的可选列表，用来配置相关后端的额外的参数
    CACHE_OPTIONS = {}    # 可选字典,在缓存类实例化期间传递，也是用来配置相关后端的额外的键值对参数
    CACHE_DEFAULT_TIMEOUT = 3600*24 # 默认过期/超时时间，单位为秒
    # CACHE_THRESHOLD=    # 缓存的最大条目数
    
    CACHE_TYPE = 'SimpleCache' # 使用本地python字典进行存储，线程非安全
    
    # CACHE_TYPE = 'filesystem' # 使用文件系统来存储缓存的值
    # CACHE_DIR = "" # 文件目录
    
    # CACHE_TYPE = 'memcached' # 使用memcached服务器缓存
    # CACHE_KEY_PREFIX # 设置cache_key的前缀
    # CAHCE_MEMCACHED_SERVERS    # 服务器地址的列表或元组
    # CACHE_MEMCACHED_USERNAME # 用户名
    # CACHE_MEMCACHED_PASSWORD # 密码
    
    # CACHE_TYPE = 'uwsgi' # 使用uwsgi服务器作为缓存
    # CACHE_UWSGI_NAME # 要连接的uwsgi缓存实例的名称
    
    # CACHE_TYPE = 'redis' # 使用redis作为缓存
    # CACHE_KEY_PREFIX # 设置cache_key的前缀
    # CACHE_REDIS_HOST  # redis地址
    # CACHE_REDIS_PORT  # redis端口
    # CACHE_REDIS_PASSWORD # redis密码
    # CACHE_REDIS_DB # 使用哪个数据库


    # 默认日志等级
    LOG_LEVEL = logging.WARN
    # flask-mail配置
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_PORT = 465
    MAIL_USERNAME = '123@qq.com'
    MAIL_PASSWORD = 'XXXXX'  # 生成的授权码
    MAIL_DEFAULT_SENDER = MAIL_USERNAME

    # 插件配置，填写插件的文件名名称，默认不启用插件。
    PLUGIN_ENABLE_FOLDERS = []

    # 配置多个数据库连接的连接串写法示例
    # HOSTNAME: 指数据库的IP地址、USERNAME：指数据库登录的用户名、PASSWORD：指数据库登录密码、PORT：指数据库开放的端口、DATABASE：指需要连接的数据库名称
    # MSSQL:    f"mssql+pymssql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=cp936"
    # MySQL:    f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"
    # Oracle:   f"oracle+cx_oracle://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}"
    # SQLite    "sqlite:/// database.db"
    # Postgres f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}"
    # Oracle的第二种连接方式
    # dsnStr = cx_Oracle.makedsn({HOSTNAME}, 1521, service_name='orcl')
    # connect_str = "oracle://%s:%s@%s" % ('{USERNAME}', ' {PASSWORD}', dsnStr)

    #  在SQLALCHEMY_BINDS 中设置：'{数据库连接别名}': '{连接串}'
    # 最后在models的数据模型class中，在__tablename__前设置        __bind_key__ = '{数据库连接别名}'  即可，表示该数据模型不使用默认的数据库连接，改用“SQLALCHEMY_BINDS”中设置的其他数据库连接
    #  SQLALCHEMY_BINDS = {
    #    'testMySQL': 'mysql+pymysql://test:123456@192.168.1.1:3306/test?charset=utf8',
    #    'testMsSQL': 'mssql+pymssql://test:123456@192.168.1.1:1433/test?charset=cp936',
    #    'testOracle': 'oracle+cx_oracle://test:123456@192.168.1.1:1521/test',
    #    'testSQLite': 'sqlite:///database.db
    # }
