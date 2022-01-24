from flask_migrate import Migrate

from common.extend.orm import db
# from entrance.models import model_lists

migrate = Migrate(db=db, directory='entrance/migrations')

