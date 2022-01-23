from typing import List

from common.view import Blueprint, View
from flask import jsonify

from pydantic import BaseModel, ValidationError, constr, parse_obj_as

from entrance.extend.orm import db

user = Blueprint('sys', __name__, url_prefix='/user')


@user.route('/')
class UserView(View):
    def get(self):
        pass
        # data, total = db.session.query(User.id, User.username).layui_paginate_json()
        # print(data)
        # return jsonify(data)
