from flask import render_template, request

from models import DepartmentModel
from common.utils.rights import permission_required, view_logging_required
from applications.view import index_bp


@index_bp.get('/dept/add')
@view_logging_required
@permission_required("admin:dept:add")
def add():
    return render_template('view/system/department_add.html')


@index_bp.get('/dept/edit')
@view_logging_required
@permission_required("admin:dept:edit")
def edit():
    dept_id = request.args.get("deptId", type=int)
    dept = DepartmentModel.query.get(dept_id)
    return render_template('view/system/department_edit.html', dept=dept)
