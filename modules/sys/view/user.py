from typing import List

from common.view import Blueprint,View
from flask import jsonify

from pydantic import BaseModel, ValidationError, constr, parse_obj_as

from modules.sys.models.user import User, Userschema

user = Blueprint('sys', __name__, url_prefix='/user')


@user.route('/')
class UserView(View):
    def get(self):
        u = User.query.all()
        # m = parse_obj_as(List[User], u)

        return '1'