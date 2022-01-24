import datetime
from typing import Tuple

from flask import request
from flask_sqlalchemy import SQLAlchemy, BaseQuery


class Query(BaseQuery):

    def all_json(self) -> list:
        return [dict(i) for i in self.all()]

    def soft_delete(self):
        return self.update({"delete_at": datetime.datetime.now()})

    def logic_all(self):
        return self.filter_by(delete_at=None).all()

    def layui_paginate(self):
        return self.paginate(page=request.args.get('page', type=int),
                             per_page=request.args.get('limit', type=int),
                             error_out=False)

    def layui_paginate_json(self) -> Tuple[list, int]:
        p = self.paginate(page=request.args.get('page', type=int),
                          per_page=request.args.get('limit', type=int),
                          error_out=False)

        return [dict(i) for i in p.items], p.total


db = SQLAlchemy(query_class=Query)
