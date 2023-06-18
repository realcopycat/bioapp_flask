from functools import wraps
from flask import abort, request, current_app
from applications.common.admin_log import admin_log
from flask_jwt_extended import jwt_required, current_user
from applications.common.utils.cache import cache
from applications.common.utils.http import fail_api

def authorize(power: str, log: bool = False):
    """用户权限判断，用于判断目前会话用户是否拥有访问权限

    :param power: 权限标识
    :type power: str
    :param log: 是否记录日志, defaults to False
    :type log: bool, optional
    """

    def decorator(func):
        @jwt_required()
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 定义管理员的id为1
            if current_user.username == current_app.config.get("SUPERADMIN"):
                return func(*args, **kwargs)

            if (cache.get("permissions_" + str(current_user.id)) == None) or (
                not power in cache.get("permissions_" + str(current_user.id))
            ):
                if log:
                    admin_log(request=request, is_access=False)
                if request.method == "GET":
                    abort(403)
                else:
                    return fail_api(msg="权限不足!",code=403)
            if log:
                admin_log(request=request, is_access=True)
            return func(*args, **kwargs)

        return wrapper

    return decorator


# @auth.verify_token
# def verify_token(token):
#     g.user = None
#     serializer = Serializer(current_app.config.get("SECRET_KEY"), expires_in=current_app.config.get("TOKEN_EXPIRATION"))
#     try:
#         data = serializer.loads(token)
#     # except BadSignature:
#     # # AuthFailed 自定义的异常类型
#     #     raise AuthFailed(msg='token不正确')
#     # except SignatureExpired:
#     #     raise AuthFailed(msg='token过期')
#     except:
#         return False
#     if 'username' in data:
#         g.user = data['username']
#         return True
#     return False
