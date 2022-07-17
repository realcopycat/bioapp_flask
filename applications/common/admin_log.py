from flask_login import current_user

from applications.common.utils.validate import xss_escape
from applications.extensions import db
from applications.models import AdminLog

def get_user_ip(request):
    if request.headers.get('X-Forwarded-For'):
        return request.headers['X-Forwarded-For']
    elif request.headers.get('X-Real-IP'):
        return request.headers.get('X-Real-IP')
    else:
        return request.remote_addr

def login_log(request, uid, is_access):
    info = {
        'method': request.method,
        'url': request.path,
        'ip': get_user_ip(request),
        'user_agent': xss_escape(request.headers.get('User-Agent')),
        'desc': xss_escape(request.form.get('username')),
        'uid': uid,
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
    db.session.flush()
    db.session.commit()
    return log.id


def admin_log(request, is_access):
    info = {
        'method': request.method,
        'url': request.path,
        'ip': get_user_ip(request),
        'user_agent': xss_escape(request.headers.get('User-Agent')),
        'desc': xss_escape(str(dict(request.values))),
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
