# coding:utf-8
import sys,os 
sys.path.append(os.path.realpath(os.path.dirname(os.path.realpath(__file__))))
from config.db import db
from werkzeug.security import check_password_hash
# from flask import app


""""
用户模型
1.编号
2.账号
3.密码
4.注册时间
"""


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(20), nullable=False)  # 账号
    pwd = db.Column(db.String(100), nullable=False)  # 密码
    addtime = db.Column(db.DateTime, nullable=False)  # 注册时间

    def __repr__(self):
        return "<User %r>" % self.name

    def check_pwd(self,pwd):
        return check_password_hash(self.pwd,pwd)


"""
文章模型
1.编号
2.标题
3.分类
4.作者
5.封面
6.内容
7.发布时间
"""


class Art(db.Model):
    __tablename__ = 'art'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(100), nullable=False)  # 标题
    header_title = db.Column(db.String(200), nullable=True)  # 
    header_keyword = db.Column(db.String(200), nullable=True)  # 
    header_desc = db.Column(db.String(200), nullable=True)  # 
    content_desc = db.Column(db.String(200), nullable=True)  # 
    cate = db.Column(db.Integer, nullable=False)  # 分类
    user_id = db.Column(db.Integer, nullable=False)  # 作者ID
    logo = db.Column(db.String(100), nullable=True)  # LOGO
    content = db.Column(db.Text, nullable=False)  # 内容
    addtime = db.Column(db.DateTime, nullable=False)  # 发布时间

    def __repr__(self):
        return "<Art %r>" % self.title


if __name__ == '__main__':
    
    db.create_all()
