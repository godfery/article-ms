# coding:utf-8
from flask import Flask
import os
# import sys



app = Flask(__name__,instance_path=os.path.join(os.path.dirname(__file__), '../'))
app.root_path = os.path.join(os.path.dirname(__file__), '../')
app.config['SECRET_KEY'] = '12345678'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@127.0.0.1:3306/article_web"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UP'] = os.path.join(app.root_path, 'static/uploads')
if __name__ == '__main__':
    print(app.config['UP'])
