from flask import Blueprint, render_template

document_bp = Blueprint('document', __name__)


@document_bp.route('/component/code/index.html')
def component_code():
    return render_template('component/code/index.html')


@document_bp.route('/view/<document>/<file>')
def document_view(document, file):
    return render_template(f'view/{document}/{file}')


@document_bp.get('/login.html')
def login_html():
    return render_template('login.html')
