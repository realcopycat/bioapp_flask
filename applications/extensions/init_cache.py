
from flask import Flask
from applications.common.utils.cache import init_cache

def register_cache(app: Flask):
    init_cache(app)
    