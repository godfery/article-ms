# coding:utf-8

from flask_sqlalchemy import SQLAlchemy
from config.manager import app
db = SQLAlchemy(app)