# coding:utf-8

import datetime
from flask import render_template, redirect, url_for, request,flash
from config.manager import app
# from models.models import db
from models.category import Category,db
from route.func import user_login_required
from route.forms import CatEditForm,CatForm


# 发布文章
@app.route('/cat/add/', methods=['GET', 'POST'])
@user_login_required
def cat_add():
    form = CatForm()
    if form.validate_on_submit():
        data = form.data
       
        # 保存数据
        art = Category(
            name=data['name'],
            addtime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )
        db.session.add(art)
        db.session.commit()
        flash(u'提交成功', 'ok')
        form.name.data = ""
    return render_template('category_add.html', title=u"增加分类", form=form)


# 编辑文章
@app.route('/cat/edit/<int:id>/', methods=['GET', 'POST'])
@user_login_required
def cat_edit(id):
    art = Category.query.get_or_404(ident=id)
    form = CatEditForm()
    if form.validate_on_submit():
        
        art.name = form.name.data
        print(art.name)
        
        # art.logo = logo
        db.session.add(art)
        db.session.commit()
        flash(u'编辑成功')
        return redirect(request.args.get('next') or url_for('cat_list', page=1))
    # 这一段不要放在POST前面，因为会覆盖修改后的数据，因为会覆盖修改后的数据，因为会覆盖修改后的数据！
    form.name.data = art.name
    return render_template('category_edit.html', form=form, title=u'编辑文章')


# 删除文章
@app.route('/cat/del/<int:id>/', methods=['GET'])
@user_login_required
def cat_del(id):
    art = Category.query.get_or_404(ident=id)
    db.session.delete(art)
    db.session.commit()
    flash(u'删除 %s 成功' % art.title)
    return redirect(request.args.get('next') or url_for('cat_list', page=1))


# 文章列表
@app.route('/cat/list/<int:page>/', methods=['GET'])
@user_login_required
def cat_list(page):
    if page is None:
        page = 1
    
    page_data = Category.query.order_by(
        Category.addtime.desc()
    ).paginate(page=page, per_page=10)
    cate = [(1, u'科技'), (2, u'搞笑'), (3, u'军事')]
    return render_template('category_list.html', title=u"分类列表", page_data=page_data, cate=cate)

