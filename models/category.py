# coding:utf-8
from flask_sqlalchemy import SQLAlchemy
from config.manager import app
from config.db import db


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(20), nullable=False)  # 账号
    addtime = db.Column(db.DateTime, nullable=False)  # 注册时间

    def __repr__(self):
        return "<User %r>" % self.name


if __name__ == '__main__':
    db.create_all()
