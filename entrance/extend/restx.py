from flask import Blueprint
from flask_restx import Api

from entrance.namespaces import namespaces

sys = Blueprint('sys', __name__, url_prefix='/sys')

api = Api(sys, version='1.0', title='Pear Admin Flask',
          description='admin based on flask and layui',
          )
for i in namespaces:
    api.add_namespace(i)
