# coding:utf-8
import datetime
import os
import uuid
from flask import render_template, redirect, url_for, flash, session, Response, request,Flask
from functools import wraps

def user_login_required(f):
    @wraps(f)
    def login_req(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)

    return login_req

# 修改文件名称
def chang_name(filename):
    info = os.path.splitext(filename)
    # 文件名：时间格式字符串+唯一字符串+后缀名
    filename = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + uuid.uuid4().hex + info[-1]
    return filename