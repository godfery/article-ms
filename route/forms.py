# coding:utf-8
from flask import session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField, SelectField,IntegerField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from models.models import User
from route.func import get_category


"""
登录表单：
1.账号
2.密码
3.登录按钮
"""


class LoginForm(FlaskForm):
    name = StringField(
        label=u"账号",
        validators=[
            DataRequired(u'账号不能为空')
        ],
        description=u"账号",
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入账号'
        }
    )
    pwd = PasswordField(
        label=u"密码",
        validators=[
            DataRequired(u'密码不能为空')
        ],
        description=u'密码',
        render_kw={
            'class': 'form-control',
            'placeholder': u'请输入密码'
        }
    )
    submit = SubmitField(
        u'登录',
        render_kw={
            'class': 'btn btn-primary'
        }
    )

    def validate_pwd(self, field):
        pwd = field.data
        user = User.query.filter_by(name=self.name.data).first()
        if user is not None and not user.check_pwd(pwd):
            raise ValidationError(u'密码错误')

    def validate_name(self, field):
        name = field.data
        user = User.query.filter_by(name=name).first()
        if not user:
            raise ValidationError(u'不存在的用户名')


"""
注册表单：
1.账号
2.密码
3.确认密码
4.验证码
5.注册按钮
"""


class RegisterForm(FlaskForm):
    name = StringField(
        label=u"账号",
        validators=[
            DataRequired(u'账号不能为空')
        ],
        description=u"账号",
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入账号'
        }
    )
    pwd = PasswordField(
        label=u"密码",
        validators=[
            DataRequired(u'密码不能为空')
        ],
        description=u'密码',
        render_kw={
            'class': 'form-control',
            'placeholder': u'请输入密码'
        }
    )
    repwd = PasswordField(
        label=u"确认密码",
        validators=[
            DataRequired(u'确认密码不能为空'),
            EqualTo('pwd', message=u'两次输入密码不一致')
        ],
        description=u'确认密码',
        render_kw={
            'class': 'form-control',
            'placeholder': u'确认请输入密码'
        }
    )
    code = StringField(
        label=u'验证码',
        validators=[
            DataRequired(u'验证码不能为空')
        ],
        description=u'验证码',
        render_kw={
            'class': 'form-control',
            'placeholder': u'请输入验证码'
        }
    )
    submit = SubmitField(
        u'注册',
        render_kw={
            'class': 'btn btn-success'
        }
    )

    def validate_name(self, field):
        name = field.data
        user = User.query.filter_by(name=name).first()
        if user:
            raise ValidationError(u'账号已存在，不能重复注册')

    def validate_code(self, field):
        codes = field.data.lower()
        if session.get('codes') is None or codes != session['codes']:
            raise ValidationError(u'验证码错误')


"""
发布文章表单
1.标题
2.分类
3.封面
4.内容
5.发布文章按钮
"""


class ArtForm(FlaskForm):
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
    header_title = StringField(
        label=u'seo标题',
        description=u'seo标题',
        
        render_kw={
            'class': 'form-control',
            'placeholder': u'请输入'
        }
    )
    header_keyword = StringField(
        label=u'seo关键字',
        description=u'seo关键字',
        
        render_kw={
            'class': 'form-control',
            'placeholder': u'请输入'
        }
    )
    header_desc = StringField(
        label=u'seo描述',
        description=u'seo描述',
        
        render_kw={
            'class': 'form-control',
            'placeholder': u'请输入'
        }
    )
    content_desc = StringField(
        label=u'内容概要',
        description=u'内容概要',
        validators=[
            DataRequired(u'内容概要不能为空')
        ],
        render_kw={
            'class': 'form-control',
            'placeholder': u'请输入内容概要'
        }
    )

    cate = SelectField(
        label=u'分类',
        description=u'分类',
        validators=[],
        choices=get_category(),
        default=3,
        coerce=int,
        render_kw={
            'class': 'form-control'
        }
    )
    logo = FileField(
        label=u'封面',
        description=u'封面',
        render_kw={
            'class': 'form-control-file'
        }
    )
    content = TextAreaField(
        label=u'内容',
        description=u'内容',
        validators=[
            DataRequired(u'内容不能为空')
        ],
        render_kw={
            'style': 'height:300px;',
            'id': 'content'
        }
    )
    submit = SubmitField(
        u'发布文章',
        render_kw={
            'class': 'btn btn-primary'
        }
    )


class ArtEditForm(FlaskForm):
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
    header_title = StringField(
        label=u'seo标题',
        description=u'seo标题',
        
        render_kw={
            'class': 'form-control',
            'placeholder': u'请输入'
        }
    )
    header_keyword = StringField(
        label=u'seo关键字',
        description=u'seo关键字',
        
        render_kw={
            'class': 'form-control',
            'placeholder': u'请输入'
        }
    )
    header_desc = StringField(
        label=u'seo描述',
        description=u'seo描述',
        
        render_kw={
            'class': 'form-control',
            'placeholder': u'请输入'
        }
    )
    content_desc = StringField(
        label=u'内容概要',
        description=u'内容概要',
        validators=[
            DataRequired(u'内容概要不能为空')
        ],
        render_kw={
            'class': 'form-control',
            'placeholder': u'请输入内容概要'
        }
    )
    cate = SelectField(
        label=u'分类',
        description=u'分类',
        validators=[],
        choices=get_category(),
        default=3,
        coerce=int,
        render_kw={
            'class': 'form-control'
        }
    )
    
    content = TextAreaField(
        label=u'内容',
        description=u'内容',
        validators=[
            DataRequired(u'内容不能为空')
        ],
        render_kw={
            'style': 'height:300px;',
            'id': 'content'
        }
    )
    submit = SubmitField(
        u'保存更改',
        render_kw={
            'class': 'btn btn-primary'
        }
    )


class CatForm(FlaskForm):
    name = StringField(
        label=u'分类名字',
        description=u'分类名字',
        validators=[
            DataRequired(u'分类名字不能为空')
        ],
        render_kw={
            'class': 'form-control',
            'placeholder': u'请输入'
        }
    )
    
    submit = SubmitField(
        u'提交分类',
        render_kw={
            'class': 'btn btn-primary'
        }
    )


class CatEditForm(FlaskForm):
    name = StringField(
        label=u'分类名字',
        description=u'分类名字',
        validators=[
            DataRequired(u'分类名字不能为空')
        ],
        render_kw={
            'class': 'form-control',
            'placeholder': u'请输入'
        }
    )
    
    submit = SubmitField(
        u'保存更改',
        render_kw={
            'class': 'btn btn-primary'
        }
    )