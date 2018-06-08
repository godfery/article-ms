# coding:utf-8

import datetime
from flask import render_template, redirect, url_for, request,flash
from config.manager import app
# from models.models import db
from models.template import Template,db
from route.func import user_login_required
from route.templateForms import TemplateEditForm,TemplateForm


# 发布文章
@app.route('/template/add/', methods=['GET', 'POST'])
@user_login_required
def template_add():
    form = TemplateForm()
    if form.validate_on_submit():
        data = form.data
       
        # 保存数据
        temp = Template(
            title=data['title'],
            saveName=data['saveName'],
            toPath=data['toPath'],
            content=data['content'],
            addtime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )
        db.session.add(temp)
        db.session.commit()
        flash(u'提交成功', 'ok')
        # form..data = ""
    return render_template('template_add.html', title=u"增加模版", form=form)


# 编辑文章
@app.route('/template/edit/<int:id>/', methods=['GET', 'POST'])
@user_login_required
def template_edit(id):
    tem = Template.query.get_or_404(ident=id)
    form = TemplateEditForm()
    if form.validate_on_submit():
        print(form.content.data)
        tem.title = form.title.data
        tem.saveName = form.saveName.data
        tem.toPath = form.toPath.data
        tem.content = form.content.data
    
        
        db.session.add(tem)
        db.session.commit()
        flash(u'编辑成功')
        return redirect(request.args.get('next') or url_for('template_list', page=1))
    # 这一段不要放在POST前面，因为会覆盖修改后的数据，因为会覆盖修改后的数据，因为会覆盖修改后的数据！
    form.title.data = tem.title
    form.saveName.data = tem.saveName
    form.toPath.data = tem.toPath
    form.content.data = tem.content

    return render_template('template_edit.html', form=form, title=u'编辑模版')


# 删除文章
@app.route('/template/del/<int:id>/', methods=['GET'])
@user_login_required
def template_del(id):
    art = Template.query.get_or_404(ident=id)
    db.session.delete(art)
    db.session.commit()
    flash(u'删除 %s 成功' % art.title)
    return redirect(request.args.get('next') or url_for('template_list', page=1))

# 删除文章
@app.route('/template/gen/<int:id>/', methods=['GET'])
@user_login_required
def template_gen(id):
    art = Template.query.get_or_404(ident=id)
    # db.session.delete(art)
    # db.session.commit()
    
    # flash(u'删除 %s 成功' % art.title)
    from route.func import write_to_file_path

    write_to_file_path(art.saveName,art.content,art.toPath)

    flash(u'生成 %s 成功,文件名 %s' % (art.title,art.saveName))
    return redirect(request.args.get('next') or url_for('template_list', page=1))

# 文章列表
@app.route('/template/list/<int:page>/', methods=['GET'])
@user_login_required
def template_list(page):
    if page is None:
        page = 1
    
    page_data = Template.query.order_by(
        Template.addtime.desc()
    ).paginate(page=page, per_page=10)
    
    return render_template('template_list.html', title=u"模版列表", page_data=page_data)

