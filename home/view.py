#-*-coding:utf-8-*-
# 刘文豪
# 大帅哥
import os
import requests
from werkzeug.utils import secure_filename
from os import path
from pyecharts import options as opts  # 统计图模块
from pyecharts.charts import Bar, Pie, Line  # # 统计图模块
import time
import random
from tool import Password, OnlySign, set_img
from flask import Flask, url_for, redirect, views, request, session, Response, make_response  # 从Flask框架导入Flask框架
from flask import render_template, flash, jsonify, send_from_directory
from . import home
from .form import LoginForm, PostForm, ForgetPassword, NewPassword, User_edit, WriteForm, ReplyForm, ReplyuserForm, SearchForm, SentForm, Sentlivelife
from models import User, queryStudent, queryStudent2, addstudent, queryEmail, editPassword, editPassword2, QueryDate, QueryMatch, QueryReply, QueryVP, QueryPM, QueryLvLf  # 应用
from flask_mail import Message
from exts import mail


@home.route("/", methods=['GET', 'POST'])  # 首页
def index():
    result = os.listdir('C:\\NX\Bolg\static\zy')
    form = SearchForm()
    title = request.form.get("message")
    page = int(request.args.get('page', 1))
    pagination = QueryMatch().query(page)
    query = pagination.items  # 实现文章分页
    name = request.cookies.get("user")
    paw = str(request.cookies.get("user_pw"))
    q = queryStudent(name, Password(paw).deciphering())
    q2 = queryStudent2()
    r = QueryReply().query()
    v = QueryVP().query()
    url = url_for('nxapiapp.get_soup')
    data = requests.get("http://127.0.0.1:7000" + url)
    data.encoding = 'utf8'
    message = data.text
    if form.validate_on_submit():
        pagination = QueryMatch().dimquery(title, page)
        query = pagination.items  # 实现文章分页
        return render_template("index/index.html", q=q, q2=q2, r=r, v=v, query=query, pagination=pagination, form=form, result=result, message=message)
    return render_template("index/index.html", q=q, q2=q2, r=r, v=v, query=query, pagination=pagination, form=form, result=result, message=message)


@home.route("/quit", methods=['GET', 'POST'])
def off():
    QueryDate().edit2("0", int(Password(request.cookies.get("user_id")).deciphering()))
    resp = make_response(redirect(url_for("homeapp.login")))
    resp.delete_cookie("user")
    resp.delete_cookie("user_id")
    resp.delete_cookie("user_pw")
    session['student'] = False
    return resp


@home.route("/recommend", methods=['GET', 'POST'])  # 首页
def indextui():
    page = int(request.args.get('page', 1))
    pagination = QueryMatch().query(page)
    query = pagination.items  # 实现文章分页
    name = request.cookies.get("user")
    paw = str(request.cookies.get("user_pw"))
    q = queryStudent(name, Password(paw).deciphering())
    q2 = queryStudent2()
    r = QueryReply().query()
    v = QueryVP().query()
    return render_template("index/indextuijian.html", q=q, q2=q2, r=r, v=v, query=query, pagination=pagination)

@home.route("/<int:post_id>", methods=['GET', 'POST'])
def match(post_id):
    if session.get('student') == True:
        form = ReplyForm()
        name = request.cookies.get("user")
        paw = str(request.cookies.get("user_pw"))
        q = queryStudent(name, Password(paw).deciphering())
        q2 = queryStudent2()
        r = QueryReply().query()
        v = QueryVP().query()
        body = QueryMatch().query2(post_id)
        seenum = QueryMatch().queryseenum(post_id).seenum
        seenum = int(seenum) + 1
        QueryMatch().editseenum(post_id, str(seenum))
        user_id1 = int(Password(request.cookies.get("user_id")).deciphering())
        body1 = request.form.get("body")
        replynum = QueryReply().query2(post_id)
        QueryMatch().editreply(post_id, replynum)
        if form.validate_on_submit():
            QueryReply().add(user_id1, post_id, body.user_id, 0, body1)
            return redirect(url_for("homeapp.match", post_id=post_id))
        else:
            return render_template("index/match.html", body=body, q=q, q2=q2, r=r, v=v, form=form, post_id=post_id)
    else:
        return "<h1>请先登入，谢谢</<h1>"


@home.route("/reply/<int:match_id>/<int:replyuser_id>/<int:replyself_id>", methods=['GET', 'POST'])
def reply(match_id, replyuser_id, replyself_id):
    form = ReplyuserForm()
    user_id1 = int(Password(request.cookies.get("user_id")).deciphering())
    if form.validate_on_submit():
        QueryReply().add(user_id1, match_id, replyuser_id, replyself_id, request.form.get("body"))
        return redirect(url_for("homeapp.match", post_id=match_id))
    else:
        return render_template("user/reply.html", form=form)


@home.route("/sent/<int:user_id>/<int:recevice_id>/<int:match_id>", methods=['GET', 'POST'])
def sentEM(user_id, recevice_id, match_id):
    form = SentForm()
    if form.validate_on_submit():
        Sign = OnlySign().carry()
        for i in QueryPM().queryall():
            if len(QueryPM().querySign(Sign)) > 0:
                Sign = OnlySign().carry()
            if (user_id == i.user_id and recevice_id == i.recevice_id) or (
                    user_id == i.recevice_id and recevice_id == i.user_id):
                Sign = i.onlySigns
        QueryPM().add(user_id, recevice_id, request.form.get("body"), Sign, 0)
        return redirect(url_for("homeapp.match", post_id=match_id))
    return render_template("user/sentEM.html", form=form)


@home.route("/login", methods=['GET', 'POST'])
def login():  # 登入页面
    form = LoginForm()
    if form.validate_on_submit():
        name = request.form.get('username')
        password = request.form.get('userPassword')
        word = request.form.get('wordPassword')
        print(session.get('image'))
        if queryStudent(name, password) and word == session.get('image'):
            session['student'] = True
            session.permanent = True
            id = queryStudent(name, password)[0].id
            QueryDate().edit2("1", id)
            r = make_response(redirect(url_for('homeapp.index')))
            r.set_cookie("user", name)
            P = Password(str(id))
            P2 = Password(str(password))
            ID = P.encryption()
            PW = P2.encryption()
            tj = QueryMatch().queryall()
            ty = QueryDate().queryuser(id)
            seenum = 0
            disnum = 0
            idnum = 0
            lovenum = 0
            for qd in tj:
                if id == qd.user_id:
                    idnum = idnum + 1
                    seenum = seenum + int(qd.seenum)
                    lovenum = lovenum + int(qd.love)
                    disnum = disnum + int(qd.disnum)
                else:
                    pass
            QueryDate().edit(disnum=str(disnum), matchnum=str(idnum), seenum=str(seenum), lovenum=str(lovenum), user_id=id)
            r.set_cookie("user_id", str(ID))
            r.set_cookie("user_pw", str(PW))
            return r
        else:
            return "密码错误或暗号错误，请返回重新登入！！！注意验证码区分大小写！！！验证码区分大小写！！！"
    else:
        return render_template('home/login.html', form=form)

@home.route('/post', methods=['GET', 'POST'])
def post():  # 注册界面
    form = PostForm()
    if request.method == "POST":
        name = request.form.get('username')
        password = request.form.get('userPassword')
        email = request.form.get("email")
        if form.validate_on_submit():
            if queryEmail(email) > 0:
                return "<h1>已经存在该用户请直接返回登入，如忘记密码则直接找回密码</h1>"
            addstudent(name, password, email)
            a = queryStudent(name, password)
            user_id = a[0].id
            QueryVP().add(user_id, vip=0, tui=0, ding=0, manage=0)
            QueryDate().addall(user_id,disnum='0',matchnum='0',seenum='0',lovenum='0',online='1')
            flash("欢迎加入，注册成功！")
            time.sleep(2)
            return redirect(url_for("homeapp.login"))
        else:
            return render_template('home/post.html', form=form)

    else:
        return render_template('home/post.html', form=form)

@home.route("/forgetpassword", methods=['GET', 'POST'])
def forgetpassword():  # 密码找回页面
    s = ''
    for a in range(6):
        for i in str(random.randint(0, 9)):
            s = s + i
    form = ForgetPassword()
    if request.method == "POST":
        email = request.form.get("email")
        select = request.form.get("number")
        if form.validate_on_submit():
            if form.sent.data:
                if queryEmail(email) > 0:
                    message = Message(subject='极客工作室密码找回中心', recipients=['{}'.format(email)], body='您的验证码是{}'.format(s))
                    try:
                        mail.send(message)
                        p = Password(s).encryption()
                        r = Response(
                            '<h2 style="color: black; font-weight:bold; text-align: center;" >验证码发送成功，请注意查收，3分钟内有效~</h2>')
                        r.set_cookie(email, p, max_age=180)
                        r.set_cookie("need", email, max_age=180)
                        return r
                        # return '<h2 style="color: black; font-weight:bold; text-align: center;" >发送成功，请注意查收~</h2>'
                    except Exception as e:
                        print(e)
                        return '<h2 style="color: black; font-weight:bold; text-align: center;" >发送失败，请联系工作人员~</h2>'
                else:
                    return '<h2 style="color: black; font-weight:bold; text-align: center;" >不存在该用户信息，请核对邮箱</h2>'

            elif form.submit.data:
                if queryEmail(email) > 0 and select == Password(request.cookies.get(email)).deciphering():
                    rest = make_response(redirect(url_for("homeapp.newPassword")))
                    rest.set_cookie("argee", "true", max_age=180)
                    return rest
                else:
                    print(select, s)
                    return "失败"
        else:
            return render_template("home/forgetPassword.html", form=form)

    else:
        return render_template("home/forgetPassword.html", form=form)

@home.route("/newPassword", methods=['GET', 'POST'])
def newPassword():
    form = NewPassword()
    if form.validate_on_submit():
        password2 = request.form.get("password2")
        if request.cookies.get('argee') == 'true':
            editPassword(request.cookies.get('need'), password2)
            return redirect(url_for('homeapp.login'))
        else:
            return '<h1 style="color: black; font-weight:bold; text-align: center;">对不起你没有资格操作这个页面</h1>'

    else:
        return render_template('home/newPassword.html', form=form)


@home.route("/user", methods=['GET', 'POST'])
def user_ui():
    if session.get('student') == True:
        if QueryDate().queryuser(int(Password(request.cookies.get("user_id")).deciphering())):
            pass
        else:
            QueryDate().add(int(Password(request.cookies.get("user_id")).deciphering()))
        query1 = QueryDate().queryuser(int(Password(request.cookies.get("user_id")).deciphering()))
        bar = (
            Bar()
                .add_xaxis(["评论次数", "文章数量", "浏览次数", "喜欢人数"])
                .add_yaxis("显示", [int(query1.disnum), int(query1.matchnum), int(query1.seenum), int(query1.lovenum)])
                # .add_yaxis("商家B", [15, 25, 16, 55, 48, 8])
                .set_global_opts(title_opts=opts.TitleOpts(title="Bar-统计", subtitle="数量"))
        )
        pie = (
            Pie()
                .add("", [("评论次数", int(query1.disnum)), ("文章数量", int(query1.matchnum)), ("浏览次数", int(query1.seenum)), ("喜欢人数", int(query1.lovenum))])
                .set_global_opts(title_opts=opts.TitleOpts(title="Pie-统计"))
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))

        )
        line = (
            Line()
                .add_xaxis(["评论次数", "文章数量", "浏览次数", "喜欢人数"])
                .add_yaxis('关系图', [int(query1.disnum), int(query1.matchnum), int(query1.seenum), int(query1.lovenum)], is_smooth=True)
                .set_global_opts(title_opts=opts.TitleOpts(title='折线图', subtitle='数量'))

        )

        pw = Password(request.cookies.get("user_pw")).deciphering()
        query = queryStudent(request.cookies.get("user"), pw)
        return render_template("index/user_ui.html", query=query, bar_options=bar.dump_options(), pie_options=pie.dump_options(),
                               line_options=line.dump_options(), query1=query1)
    else:
        return "<h1>请先登入，谢谢</<h1>"


@home.route("/user/self", methods=['GET', 'POST'])
def userself():
    if session.get('student') == True:
        name = request.cookies.get("user")
        paw = str(request.cookies.get("user_pw"))
        q = queryStudent(name, Password(paw).deciphering())
        q2 = queryStudent2()
        r = QueryReply().query()
        v = QueryVP().query()
        m = QueryMatch().queryall()
        if QueryDate().queryuser(int(Password(request.cookies.get("user_id")).deciphering())):
            pass
        else:
            QueryDate().add(int(Password(request.cookies.get("user_id")).deciphering()))
        query1 = QueryDate().queryuser(int(Password(request.cookies.get("user_id")).deciphering()))
        bar = (
            Bar()
                .add_xaxis(["评论次数", "文章数量", "浏览次数", "喜欢人数"])
                .add_yaxis("显示", [int(query1.disnum), int(query1.matchnum), int(query1.seenum), int(query1.lovenum)])
                # .add_yaxis("商家B", [15, 25, 16, 55, 48, 8])
                .set_global_opts(title_opts=opts.TitleOpts(title="Bar-统计", subtitle="数量"))
        )
        pie = (
            Pie()
                .add("", [("评论次数", int(query1.disnum)), ("文章数量", int(query1.matchnum)), ("浏览次数", int(query1.seenum)),
                          ("喜欢人数", int(query1.lovenum))])
                .set_global_opts(title_opts=opts.TitleOpts(title="Pie-统计"))
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))

        )
        line = (
            Line()
                .add_xaxis(["评论次数", "文章数量", "浏览次数", "喜欢人数"])
                .add_yaxis('关系图', [int(query1.disnum), int(query1.matchnum), int(query1.seenum), int(query1.lovenum)],
                           is_smooth=True)
                .set_global_opts(title_opts=opts.TitleOpts(title='折线图', subtitle='数量'))

        )
        return render_template("user/self.html", q=q, q2=q2, r=r, v=v, bar_options=bar.dump_options(), pie_options=pie.dump_options(),
                                   line_options=line.dump_options(), m=m)
    else:
        return "<h1>请先登入，谢谢</<h1>"

@home.route("/user/edit", methods=['GET', 'POST'])
def user_edit():
    form = User_edit()
    pw = Password(request.cookies.get("user_pw")).deciphering()
    query = queryStudent(request.cookies.get("user"), pw)
    if form.upload.data:
        f = request.files.get('file')
        filename = secure_filename(f.filename)
        ext = filename.split('.', 1)[1]
        unix_time = int(time.time())
        new_filename = str(unix_time) + '.' + ext
        load = url_for('static', filename=r'img/user/head')
        new_load = "./." + load
        h_load = path.join(new_load, new_filename).replace('\\', '/')  # 保存的地址
        new_h_load = h_load.replace("./", "../")
        f.save(h_load)
        editPassword2(request.cookies.get("user"), pw, new_h_load, request.form.get("aboutme"))
        return redirect(url_for("homeapp.user_ui"))
    return render_template("index/user_edit.html", form=form, query=query)


@home.route("/write", methods=['GET', 'POST'])
def write():
    if session.get('student') == True:
        form = WriteForm()
        vp_id = 0
        name = request.cookies.get("user")
        paw = str(request.cookies.get("user_pw"))
        q = queryStudent(name, Password(paw).deciphering())
        v = QueryVP().query()
        user_id = int(Password(request.cookies.get("user_id")).deciphering())
        for i in v:
            if user_id == i.user_id:
                vp_id = int(i.id)
        title = request.form.get("title")
        body = request.form.get("body")
        love = "0"
        disnum = "0"
        seenum = "0"
        imgurl = "0"
        if form.validate_on_submit():
            QueryMatch().add(user_id, vp_id, title, body, love, disnum, seenum, imgurl)
            return redirect(url_for("homeapp.index"))
        else:
            return render_template("user/write.html", q=q, form=form)
    else:
        return "<h1>请先登入，谢谢</<h1>"

@home.route("/livelife", methods=['GET', 'POST'])
def livelife():
    if session.get('student') == True:
        page = int(request.args.get('page', 1))
        pagination = QueryLvLf().query(page)
        query = pagination.items  # 实现文章分页
        q2 = queryStudent2()
        r = QueryReply().query()
        v = QueryVP().query()
        return render_template("user/livelife.html", query=query, pagination=pagination, q2=q2, r=r, v=v)
    else:
        return "<h1>请先登入，谢谢</<h1>"


a = []
@home.route("/editlive", methods=['GET', 'POST'])
def editlive():
    if session.get('student') == True:
        form = Sentlivelife()
        global a
        for f in request.files.getlist('file'):
            filename = secure_filename(f.filename)
            ext = filename.split('.', 1)[1]
            unix_time = int(time.time() * 1000000)
            new_filename = str(unix_time) + '.' + ext
            load = url_for('static', filename=r'img/user/livelife')
            new_load = "./." + load
            h_load = path.join(new_load, new_filename).replace('\\', '/')  # 保存的地址
            new_h_load = h_load.replace("./", "../")
            a.append(new_h_load)
            set_img(f, h_load)
        if form.validate_on_submit():
            body = request.form.get('body')
            user_name = request.cookies.get("user")
            user_id = int(Password(request.cookies.get("user_id")).deciphering())
            QueryLvLf().add(user_id, user_name, body, str(a))
            a = []
            return redirect(url_for('homeapp.livelife'))
        else:
            return render_template("user/editlife.html", form=form)
    else:
        return "<h1>请先登入，谢谢</<h1>"


@home.route("/download/<filename>", methods=['GET', 'POST'])
def downloadwj(filename):
    pathwj = "C:/NX/Bolg/static/zy"
    return send_from_directory(r"{}".format(pathwj), filename="{}".format(filename), as_attachment=True)

