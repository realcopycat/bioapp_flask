from typing import List
from flask_restx import Namespace
from modules.sys.user import userns

namespaces: List[Namespace] = [
    userns,
]
