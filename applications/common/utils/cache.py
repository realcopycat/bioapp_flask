from flask_caching import Cache

#use : from applications.common.utils.cache import cache
cache = Cache()

# 基于config实现，或者基于自己的业务情况实现
def init_cache(app):
    cache.init_app(app)

# def __getattr__(self, name):
#     return getattr(self._redis_client, name)

# def __getitem__(self, name):
#     return self._redis_client[name]

# def __setitem__(self, name, value):
#     self._redis_client[name] = value

# def __delitem__(self, name):
#     del self._redis_client[name]


