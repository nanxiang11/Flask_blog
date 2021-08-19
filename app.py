#encoding:utf-8
# 刘文豪
# 大帅哥
from datetime import datetime
from io import BytesIO
from tool import validate_picture
from flask_ckeditor import CKEditor
from flask import Flask, url_for, redirect, views, request, make_response, session  # 从Flask框架导入Flask框架
from flask import render_template
from home import home
from admin import admin
from User import user
from NXAPI import nxapi
import config
from flask_wtf.csrf import CSRFProtect
from exts import db, mail, dropzone
app = Flask(__name__)


app.config.from_object(config)  # 配置文件初始化
CSRFProtect(app)  # 模块初始化
app.register_blueprint(home)  # 注册路由
app.register_blueprint(admin)  # 注册路由
app.register_blueprint(user)  # 注册路由
app.register_blueprint(nxapi)  # 注册路由

db.init_app(app)  # 注册数据库
with app.app_context():
    db.create_all()

mail.init_app(app)  # 配置邮件

ckeditor = CKEditor(app)  # 注册富文本编译器

dropzone.init_app(app)  # 注册dropzone



@app.route("/404")
def test():
    return render_template("home/404.html")


@app.template_filter()
def change(args):
    temp = eval(args)
    return temp


@app.template_filter()
def numcount(args):
    temp = len(args)
    return temp


@app.route('/code')
def get_code():
    image, str = validate_picture()
    # 将验证码图片以二进制形式写入在内存中，防止将图片都放在文件夹中，占用大量磁盘
    buf = BytesIO()
    image.save(buf, 'jpeg')
    buf_str = buf.getvalue()
    # 把二进制作为response发回前端，并设置首部字段
    response = make_response(buf_str)
    response.headers['Content-Type'] = 'image/gif'
    # 将验证码字符串储存在session中
    session['image'] = str
    return response


if __name__ == '__main__':

    app.run(debug=True, host='127.0.0.1', port=7000)
