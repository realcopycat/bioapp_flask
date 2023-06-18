from flask import session, current_app
# from flask_login import current_user
from flask_jwt_extended import current_user
from applications.common.utils.cache import cache

def init_template_directives(app):
    @app.template_global()
    def authorize(power):
        if current_user.username != current_app.config.get("SUPERADMIN"):

            return bool(power in cache.get("permissions_" + str(current_user.id)))
        else:
            return True
