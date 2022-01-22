import os

# mysql 配置
MYSQL_USERNAME: str = os.getenv('MYSQL_USERNAME') or "root"
MYSQL_PASSWORD: str = os.getenv('MYSQL_PASSWORD') or "123456"
MYSQL_HOST: str = os.getenv('MYSQL_HOST') or "127.0.0.1"
MYSQL_PORT: int = int(os.getenv('MYSQL_PORT') or 3306)
MYSQL_DATABASE: str = os.getenv('MYSQL_DATABASE') or "PearAdminFlask"

# mysql 数据库的配置信息
SQLALCHEMY_DATABASE_URI: str = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = False
SQLALCHEMY_POOL_RECYCLE = 8
