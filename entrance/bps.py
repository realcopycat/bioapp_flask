from flask import Flask
from typing import List
from common.view import Blueprint
from modules.sys.view.user import user

sys = Blueprint('sys', __name__, url_prefix='/sys')
sys_lists: List[Blueprint] = [
    user
]
sys.register_child_bp(sys_lists)

parent_lists: List[Blueprint] = [
    sys
]


def register_parent_bp(app: Flask):
    for bp in parent_lists:
        app.register_blueprint(bp)
