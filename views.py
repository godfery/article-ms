# coding:utf-8
import datetime, os, uuid
from flask import render_template, redirect, url_for, flash, session, Response, request,Flask
from models.manager import app
import route.index 
import route.route


if __name__ == '__main__':
    app.run(debug=True)
