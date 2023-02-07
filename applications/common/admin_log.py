from flask_login import current_user

from applications.common.utils.validate import str_escape
from applications.extensions import db
from applications.models import AdminLog


def admin_log(request, is_access):
    request_data = request.json if request.headers.get('Content-Type') == 'application/json' else request.values
    info = {
        'method': request.method,
        'url': request.path,
        'ip': get_user_ip(request),
        'user_agent': xss_escape(request.headers.get('User-Agent')),
        'desc': (str(dict(request_data))),
        'uid': current_user.id,
        'success': int(is_access)
    }
    log = AdminLog(
        url=info.get('url'),
        ip=info.get('ip'),
        user_agent=info.get('user_agent'),
        desc=info.get('desc'),
        uid=info.get('uid'),
        method=info.get('method'),
        success=info.get('success')
    )
    db.session.add(log)
    db.session.commit()
    return log.id


def admin_log(request, is_access):
    info = {
        'method': request.method,
        'url': request.path,
        'ip': request.remote_addr,
        'user_agent': str_escape(request.headers.get('User-Agent')),
        'desc': str_escape(str(dict(request.values if request.method == 'GET' else request.json))),
        'uid': current_user.id,
        'success': int(is_access)

    }
    log = AdminLog(
        url=info.get('url'),
        ip=info.get('ip'),
        user_agent=info.get('user_agent'),
        desc=info.get('desc'),
        uid=info.get('uid'),
        method=info.get('method'),
        success=info.get('success')
    )
    db.session.add(log)
    db.session.commit()

    return log.id
