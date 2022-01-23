from flask_migrate import Migrate

from entrance.extend.orm import db
# from entrance.models import model_lists   <-- 这一行不要删除
from entrance.models import model_lists

migrate = Migrate(db=db, directory='entrance/migrations')
