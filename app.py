# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return {"message": "欢迎使用 pear-admin-flask !"}
