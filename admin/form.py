#-*-coding:utf-8-*-
# 刘文豪
# 大帅哥
from flask_wtf.file import FileAllowed, FileRequired
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, Form, TextAreaField, FileField    ## WTF
from wtforms.validators import DataRequired, Length, EqualTo, Email      ## 验证器属性选项
from flask_ckeditor import CKEditorField


class SearchForm(FlaskForm):
    message = StringField("搜索", validators=[DataRequired()], render_kw={'placeholder': "输入搜索内容"})
    sent = SubmitField("搜索一下")

class Adminuser(FlaskForm):
    name = StringField("姓名", validators=[DataRequired()], render_kw={'placeholder': "输入您的姓名"})
    password = StringField("密码", validators=[DataRequired()], render_kw={'placeholder': "输入您的密码"})
    submit = SubmitField("登入")
