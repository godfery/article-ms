# coding:utf-8
import datetime
import os
import uuid
from flask import render_template, redirect, url_for, flash, session, Response, request, Flask
from functools import wraps
from models.category import Category


def get_category():
    return [(cut_department.id, cut_department.name)
            for cut_department in Category.query.order_by(Category.id).all()]


def user_login_required(f):
    @wraps(f)
    def login_req(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)

    return login_req


# 修改文件名称
def chang_name(filename):
    info = os.path.splitext(filename)
    # 文件名：时间格式字符串+唯一字符串+后缀名
    filename = datetime.datetime.now().strftime(
        '%Y%m%d%H%M%S') + uuid.uuid4().hex + info[-1]
    return filename


def html_decode(s):
    """
    Returns the ASCII decoded version of the given HTML string. This does
    NOT remove normal HTML tags like <p>.
    """
    htmlCodes = (("'", '&#39;'), ('"', '&quot;'), ('>', '&gt;'), ('<', '&lt;'),
                 ('&', '&amp;'),(' ','&nbsp;'),('"','&#34;'))
    for code in htmlCodes:
        s = s.replace(code[1], code[0])
    return s


def write_to_file(file, content):
    from unipath import Path

    p = Path(os.path.realpath(__name__))
    u = Path(p.parent, "news", file)

    u.write_file(html_decode(content))
    # print(p.parent)


def write_to_file_path(filename,content,path):
    from unipath import Path

    p = Path(path,filename)
    p.write_file(html_decode(content))
    

def getPageContent(cate,curpage,total,perpage=10):
    import math
    
    totalPage = math.ceil(total / perpage)
    prepage = curpage - 1
    if (prepage == 0):
        prepage = 1

    nextpage = curpage + 1
    if (nextpage == totalPage):
        nextpage = totalPage

    
    middlestr = ""


    if(totalPage > 5):
        if (curpage == 1):
            middlestr = "<a href='/news/" + str(cate) + "_1.html#__page'>1</a>&nbsp; \
                <a href='/news/" + str(cate) + "_2.html#__page'>2</a>&nbsp; \
                <a href='/news/" + str(cate) + "_3.html#__page'>3</a>&nbsp; \
                <a href='/news/" + str(cate) + "_4.html#__page'>4</a>&nbsp; \
                <a href='/news/" + str(cate) + "_5.html#__page'>5</a>... \
                <a href='/news/" + str(
                cate) + "_"+str(totalPage)+".html#__page'>"+str(totalPage)+"</a>&nbsp; "
        elif (curpage > 1 and curpage < totalPage - 5):
            middlestr = "<span class='current'>1</span>...&nbsp;\
                <a href='/news/" + str(cate) + "_" + str(
                curpage - 2) + ".html#__page'>" + str(
                curpage - 2) + "</a>&nbsp; \
                <a href='/news/" + str(cate) + "_" + str(
                curpage - 1) + ".html#__page'>" + str(
                    curpage - 1) + "</a>&nbsp; \
                <a href='/news/" + str(cate) + "_" + str(
                curpage ) + ".html#__page'>" + str(
                        curpage) + "</a>&nbsp; \
                <a href='/news/" + str(cate) + "_" + str(
                curpage + 1) + ".html#__page'>" + str(
                            curpage + 1) + "</a>&nbsp; \
                <a href='/news/" + str(cate) + "_" + str(
                curpage + 2) + ".html#__page'>" + str(
                                curpage + 2) + "</a>... \
                <a href='/news/" + str(cate) + "_" + str(
                                    totalPage) + ".html#__page'>" + str(
                                    totalPage) + "</a>&nbsp; "
        else:
            middlestr = "<span class='current'>1</span>...&nbsp;\
                <a href='/news/" + str(cate) + "_" + str(
                totalPage - 4) + ".html#__page'>" + str(
                totalPage - 4) + "</a>&nbsp; \
                <a href='/news/" + str(cate) + "_" + str(
                totalPage - 3) + ".html#__page'>" + str(
                    totalPage - 3) + "</a>&nbsp; \
                <a href='/news/" + str(cate) + "_" + str(
                totalPage - 2) + ".html#__page'>" + str(
                        totalPage - 2) + "</a>&nbsp; \
                <a href='/news/" + str(cate) + "_" + str(
                totalPage -1) + ".html#__page'>" + str(
                            totalPage - 1) + "</a> \
                <a href='/news/" + str(cate) + "_" + str(
                totalPage ) + ".html#__page'>" + str(
                                totalPage) + "</a>&nbsp; "
    else:
        for aa in range(1,totalPage+1):
            middlestr = "<a href='/news/" + str(cate) + "_"+str(aa)+".html#__page'>"+str(aa)+"</a>&nbsp;"


    firststr = "<a href='/news/" + str(
        cate) + "_1.html#__page'>首页</a>&nbsp; \
            <a href='/news/" + str(cate) + "_" + str(
            prepage) + ".html#__page'>&laquo;上一页</a>&nbsp;  "

    endstr = "        <a href='/news/" + str(cate) + "_" + str(
        nextpage) + ".html#__page'>下一页&raquo;</a>&nbsp; \
            <a href='/news/" + str(cate) + "_" + str(
            totalPage) + ".html#__page'>尾页</a> \
            <a href='#__page' id='__page' style='border:none;'>共 \
            <b>" + str(total) + "</b>条&nbsp;&nbsp; \
            <b style='color:#900;'>" + str(curpage) + "</b>/" + str(
                totalPage) + "</a>"
    # print(firststr + middlestr + endstr)
    return firststr + middlestr + endstr
