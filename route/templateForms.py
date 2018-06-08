# coding:utf-8
from flask import session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField, SelectField,IntegerField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from models.models import User
from route.func import get_category




class TemplateForm(FlaskForm):
    title = StringField(
        label=u'标题',
        description=u'标题',
        validators=[
            DataRequired(u'标题不能为空')
        ],
        render_kw={
            'class': 'form-control',
            'placeholder': u'请输入标题'
        }
    )
    
    saveName = StringField(
        label=u'保存的名字',
        description=u'保存的名字(带后缀名)',
        validators=[
            DataRequired(u'不能为空')
        ],
        render_kw={
            'class': 'form-control',
            'placeholder': u'请输入'
        }
    )
    toPath = StringField(
        label=u'保存的目录地址',
        description=u'保存的目录地址',
        validators=[
            DataRequired(u'保存的目录地址不能为空')
        ],
        render_kw={
            'class': 'form-control',
            'placeholder': u'请输入目录地址'
        }
    )

    content = TextAreaField(
        label=u'内容',
        description=u'内容',
        validators=[
            DataRequired(u'内容不能为空')
        ],
        render_kw={
            'style': 'height:300px;width:800px',
            'id': 'content'
        }
    )
    submit = SubmitField(
        u'发布文章',
        render_kw={
            'class': 'btn btn-primary'
        }
    )


class TemplateEditForm(FlaskForm):
    title = StringField(
        label=u'标题',
        description=u'标题',
        validators=[
            DataRequired(u'标题不能为空')
        ],
        render_kw={
            'class': 'form-control',
            'placeholder': u'请输入标题'
        }
    )
    
    saveName = StringField(
        label=u'保存的名字',
        description=u'保存的名字(带后缀名)',
        validators=[
            DataRequired(u'不能为空')
        ],
        render_kw={
            'class': 'form-control',
            'placeholder': u'请输入'
        }
    )
    toPath = StringField(
        label=u'保存的目录地址',
        description=u'保存的目录地址',
        validators=[
            DataRequired(u'保存的目录地址不能为空')
        ],
        render_kw={
            'class': 'form-control',
            'placeholder': u'请输入内容概要'
        }
    )

    content = TextAreaField(
        label=u'内容',
        description=u'内容',
        validators=[
            DataRequired(u'内容不能为空')
        ],
        render_kw={
            'style': 'height:300px;width:800px',
            'id': 'content'
        }
    )
    submit = SubmitField(
        u'保存更改',
        render_kw={
            'class': 'btn btn-primary'
        }
    )


