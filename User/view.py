#-*-coding:utf-8-*-
# 刘文豪
# 大帅哥
from . import user
from tool import Password, OnlySign
from flask import Flask, url_for, redirect, views, request, session, Response, make_response  # 从Flask框架导入Flask框架
from flask import render_template, flash
from models import User, queryStudent, queryStudent2, addstudent, queryEmail, editPassword, editPassword2, QueryDate, QueryMatch, QueryReply, QueryVP, queryStudent3, dimquery, QueryPM  # 应用
from .form import SentForm
a = []
b = []
@user.route("/user/resg", methods=['GET', 'POST'])
def userresg():
    global a
    global b
    form = SentForm()
    user_id = int(Password(request.cookies.get("user_id")).deciphering())
    name = request.cookies.get("user")
    paw = str(request.cookies.get("user_pw"))
    q = queryStudent(name, Password(paw).deciphering())
    q2 = queryStudent2()
    page = int(request.args.get('page', 1))
    pagination = QueryPM().queryself(user_id, page)
    query = pagination.items  # 实现文章分页
    if request.method == "GET":
        usid = int(request.args.get("user_id", 0))
        re = int(request.args.get("re", 0))
        if usid != 0 and re != 0:
            a.append(usid)
            a.append(re)
            QueryPM().edit(a[1], a[0], user_id, tfred=1)
        else:
            pass
        return render_template("user/userresg.html", query=query, q=q, q2=q2, pagination=pagination, form=form,
                               num=len(query))
    elif request.method == "POST":
        m = a[0]
        n = a[1]
        onlySigns = ''
        # QueryPM().edit(n, m, user_id, tfred=1)
        for i in QueryPM().queryall():
            if m == i.user_id and user_id == i.recevice_id :
                onlySigns = i.onlySigns

        QueryPM().add(user_id, m, request.form.get("body"), onlySigns=onlySigns, tfred=0)
        a = []
        return render_template("user/userresg.html", query=query, q=q, q2=q2, pagination=pagination, form=form,
                               num=len(query))





