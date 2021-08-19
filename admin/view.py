#-*-coding:utf-8-*-
# 刘文豪
# 大帅哥
import random
from flask import Flask, url_for, redirect, views, request, session, Response, make_response  # 从Flask框架导入Flask框架
from flask import render_template, flash
from . import admin
from .form import SearchForm, Adminuser
from models import User, queryStudent, queryStudent2, addstudent, queryEmail, editPassword, editPassword2, QueryDate, QueryMatch, QueryReply, QueryVP, queryStudent3, dimquery  # 应用


@admin.route("/admin/userinfo", methods=['GET', 'POST'])
def adminuserinfo():
    form = SearchForm()
    usermsg = queryStudent2()
    uservp = QueryVP().query()
    usermatch = QueryDate().queryuser2()
    if form.validate_on_submit():
        usermsg = dimquery(request.form.get("message"))
        return render_template("admin/adminuserinfo.html", usermsg=usermsg, uservp=uservp, usermatch=usermatch, form=form)
    else:
        return render_template("admin/adminuserinfo.html", usermsg=usermsg, uservp=uservp, usermatch=usermatch, form=form)

@admin.route("/admin/userlogin", methods=['GET', 'POST'])
def adminlogin():
    form = Adminuser()
    name = request.form.get("name")
    password = request.form.get("password")
    if form.validate_on_submit():
        if name == "super南巷" and password == "1968qwer*#%":
            return redirect(url_for("adminapp.adminuserinfo"))
        else:
            return "<h1>我们已经记录你的非法入侵，如再入侵，我们将会采取紧急措施</h1>"
    else:
        return render_template("admin/login.html", form=form)
