# coding:utf-8
import os
import datetime
import math
from flask import render_template, redirect, url_for, flash, session, Response, request
from werkzeug.security import generate_password_hash
# 用来定义一个安全的文件名称
from werkzeug.utils import secure_filename
from config.manager import app
from route.func import user_login_required
from models.models import User, db, Art
from route.forms import ArtEditForm,ArtForm,LoginForm,RegisterForm
from route.func import chang_name,get_category,write_to_file,getPageContent
# 登录装饰器


# 首页
@app.route('/')
def index():
    return redirect(url_for('login'))


# 登录
@app.route('/login/', methods=['GET', 'POST'])
def login():
    print(session.get('user'))
    if session.get('user') is not None:
        return redirect(url_for('art_list', page=1))
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        session['user'] = data['name']
        flash(u'登录成功')
        return redirect(url_for('art_list', page=1))

    return render_template('login.html', title=u"登录", form=form)


# 注册
@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        data = form.data
        name = data['name']
        pwd = generate_password_hash(data['pwd'])
        addtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        user = User(name=name, pwd=pwd, addtime=addtime)
        db.session.add(user)
        db.session.commit()
        flash(u'注册成功，请登录', 'ok')
        return redirect(url_for('login'))
    else:
        flash(u'注册失败，请重新注册', 'err')
    return render_template('register.html', title=u"注册", form=form)


# 退出
@app.route('/logout/', methods=['GET'])
@user_login_required
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))





# 发布文章
@app.route('/art/add/', methods=['GET', 'POST'])
@user_login_required
def art_add():
    form = ArtForm()
    if form.validate_on_submit():
        data = form.data
        # 上传LOGO
        logo = ""
        print(form.logo.data,"32322332")
        if form.logo.data != "":
            file = secure_filename(form.logo.data.filename)
            logo = chang_name(file)

            if not os.path.exists(app.config['UP']):
                os.makedirs(app.config['UP'])
            form.logo.data.save(app.config['UP'] + '/' + logo)
        # 获取用户ID
        user = User.query.filter_by(name=session['user']).first()
        user_id = user.id
        # 保存数据
        art = Art(
            title=data['title'],
            cate=data['cate'],
            header_title = data['header_title'],
            header_keyword = data['header_keyword'],
            header_desc= data['header_desc'],
            content_desc=data['content_desc'],
            user_id=user_id,
            logo=logo,
            content=data['content'],
            addtime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )
        db.session.add(art)
        db.session.commit()
        flash(u'发布文章成功', 'ok')
        form.title.data = ""
        form.cate.data = 1
        form.logo.data = ""
        form.content.data = ""
    return render_template('art_add.html', title=u"发布文章", form=form)


# 编辑文章
@app.route('/art/edit/<int:id>/', methods=['GET', 'POST'])
@user_login_required
def art_edit(id):
    art = Art.query.get_or_404(ident=id)
    form = ArtEditForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        
        print(form)
        art.title = form.title.data
        print(art.title)
        art.cate = form.cate.data
        art.content = form.content.data
        art.header_title = form.header_title.data
        art.header_keyword = form.header_keyword.data
        art.header_desc = form.header_desc.data
        art.content_desc = form.content_desc.data
        # art.logo = logo
        db.session.add(art)
        db.session.commit()
        flash(u'编辑成功')
        return redirect(request.args.get('next') or url_for('art_list', page=1))
    # 这一段不要放在POST前面，因为会覆盖修改后的数据，因为会覆盖修改后的数据，因为会覆盖修改后的数据！
    form.title.data = art.title
    form.cate.data = art.cate
    form.content.data = art.content
    form.header_title.data = art.header_title
    form.header_keyword.data = art.header_keyword
    form.header_desc.data = art.header_desc
    form.content_desc.data = art.content_desc

    return render_template('art_edit.html', form=form, title=u'编辑文章')


@app.template_filter('getYearMonth')
def getYearMonth_filter(s):
    if (type(s) == datetime.datetime):
        a = s.strftime('%Y-%m-%d')
        return a[0:7:]
    else:
        return s[0:7:]


@app.template_filter('getDay')
def getDay_filter(s):
    if (type(s) == datetime.datetime):
        a = s.strftime('%Y-%m-%d')
        return a[8:10:]
    else:
        return s[8:10:]


# 编辑文章
@app.route('/art/gen/<int:id>/', methods=['GET', 'POST'])
@user_login_required
def art_gen(id):
    from util.pageContext import PageContext
    category = get_category()


    
    for cat in category:
        # print(cat[0])
        totalField = Art.query.filter_by(cate=cat[0]).order_by(Art.addtime.desc()).all()
        # print(totalField)
        total = len(totalField)
        # print(total)
        totalPage = math.ceil(total / 10)
        
        pageContext = PageContext(totalField)

        

        for i in range(1, totalPage + 1):

            
            pageContent = getPageContent(cat[0],i,total,10)

            page_data = Art.query.filter_by(cate=cat[0]).order_by(Art.addtime.desc()).paginate(page=i, per_page=10)
            # print(page_data.items)

            for single in page_data.items:
                art = single
                
                pageCon = pageContext.getPageContext(art.id)
                # art = Art.query.get_or_404(ident=single.id)

                resp = render_template('design/new_body.html', title=u'编辑文章',art=art,category=category,pageContext=pageCon)

                write_to_file("%d.html" % art.id,resp)
            


            
            # from unipath import Path
            



            summary = render_template('design/new_list.html', title=u'编辑文章',page_data=page_data,pageContent=pageContent,category=category)
            write_to_file("%d_%d.html" % (art.cate, i), summary)
    

    
    


    # print(resp)

    return redirect(url_for('art_list',page=1))

# 删除文章
@app.route('/art/del/<int:id>/', methods=['GET'])
@user_login_required
def art_del(id):
    art = Art.query.get_or_404(ident=id)
    db.session.delete(art)
    db.session.commit()
    flash(u'删除 %s 成功' % art.title)
    return redirect(request.args.get('next') or url_for('art_list', page=1))


# 文章列表
@app.route('/art/list/<int:page>/', methods=['GET'])
@user_login_required
def art_list(page):
    if page is None:
        page = 1
    user = User.query.filter_by(name=session['user']).first()
    page_data = Art.query.filter_by(
        user_id=user.id
    ).order_by(
        Art.addtime.desc()
    ).paginate(page=page, per_page=10)
    cate = get_category()
    print(cate)
    return render_template('art_list.html', title=u"文章列表", page_data=page_data, cate=cate)


# 验证码
@app.route('/codes/', methods=['GET'])
def codes():
    from codes import Codes
    c = Codes()
    info = c.create_code()
    image = os.path.join(app.root_path, 'static/codes') + '/' + info['img_name']
    with open(image, 'rb') as f:
        image = f.read()
        print(image)
    session['codes'] = info['codes']
    return Response(image, mimetype='jpeg')
