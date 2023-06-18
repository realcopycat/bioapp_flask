from flask import Flask, redirect, request,abort,jsonify
from flask_jwt_extended import JWTManager
from applications.common.utils.http import fail_api
from applications.common.utils.cache import cache
from applications.models.admin_user import UserCacheInfo

jwt = JWTManager()

def register_jwt(app: Flask):
    from applications.models import User

    # app.config["JWT_SECRET_KEY"]="" # 已经写到配置文件里了

    jwt.init_app(app) # flask 使用 jwt（三）：flask-jwt-extended 使用 https://juejin.cn/post/7234450312726691898

    # 注册一个回调函数，在访问受保护的路由时从数据库自动加载用户（current_user）。
    # 这应该在成功查找时返回任何 python 对象，或者如果查找因任何原因失败（例如，如果用户已从数据库中删除）则返回 None。
    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"] # userId
        userinfo = cache.get("current_user_" + str(identity))
        if userinfo != None:
            return userinfo
        else:
            # 查缓存是否存在，存在就拿缓存，不存在就读数据库并缓存
            user = User.query.filter_by(id=identity).one_or_none()
            userinfo = UserCacheInfo(user.id,user.username)
            cache.set("current_user_" + str(user.id), userinfo)

            return userinfo

    # 注册一个回调函数，该函数在使用 create_access_token 创建 JWT 时将传入的任何对象作为身份，并将其转换为 JSON 可序列化格式。
    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user.id

    @jwt.expired_token_loader
    def my_expired_token_callback(jwt_header, jwt_payload):
        if request.method == "GET":
            return redirect("/passport/login")
        
        return fail_api(msg="token 已失效",code=401)

        
