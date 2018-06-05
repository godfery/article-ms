# coding:utf-8
import datetime
import os
import uuid
from flask import render_template, redirect, url_for, flash, session, Response, request,Flask
from functools import wraps
from models.category import Category


def get_category():
    return [(cut_department.id, cut_department.name)  for cut_department in Category.query.order_by(Category.id).all()] 

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

def html_decode(s):
    """
    Returns the ASCII decoded version of the given HTML string. This does
    NOT remove normal HTML tags like <p>.
    """
    htmlCodes = (
            ("'", '&#39;'),
            ('"', '&quot;'),
            ('>', '&gt;'),
            ('<', '&lt;'),
            ('&', '&amp;')
        )
    for code in htmlCodes:
        s = s.replace(code[1], code[0])
    return s



def write_to_file(file,content):
    from unipath import Path


    p = Path(os.path.realpath(__name__))
    u = Path(p.parent,"gen",file)

    u.write_file(html_decode(content))
    # print(p.parent)