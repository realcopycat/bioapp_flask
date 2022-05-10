# 个人中心
from flask import request, jsonify
from flask.views import MethodView
from flask_restful import reqparse

from common.utils.http import fail_api, success_api
from extensions import db
from models import UserModel


