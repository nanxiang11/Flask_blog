#-*-coding:utf-8-*-
# 刘文豪
# 大帅哥
from flask import flash
from flask_wtf.file import FileAllowed, FileRequired
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, Form, TextAreaField, FileField    ## WTF
from wtforms.validators import DataRequired, Length, EqualTo, Email      ## 验证器属性选项
from flask_ckeditor import CKEditorField


class LoginForm(FlaskForm):
    username = StringField('name', validators=[DataRequired(message='不能为空')], render_kw={'placeholder': "请输入你的真实姓名！"})
    userPassword = PasswordField('password', validators=[DataRequired(), Length(6, 6, message="密码位数不对！请重新输入")], render_kw={'placeholder': "请输入您的密码！"})
    wordPassword = StringField('word', validators=[DataRequired()], render_kw={'placeholder': "验证码"})
    submit = SubmitField('登入')

class PostForm(FlaskForm):
    username = StringField('name', validators=[DataRequired(message='不能为空')], render_kw={'placeholder': "请输入你的真实姓名！"})
    userPassword = PasswordField('password', validators=[DataRequired(), Length(6, 6, message="密码位数不对！请重新输入")],
                                 render_kw={'placeholder': "请输入您的密码！"})
    newuserPassword = PasswordField('password', validators=[DataRequired(), Length(6, 6, message="密码位数不对！请重新输入"), EqualTo('userPassword', "两次密码填写不一样")],
                                 render_kw={'placeholder': "请再次输入您的密码！"})
    email = StringField('email', validators=[DataRequired(message='不能为空')],  render_kw={'placeholder': "请输入你的邮箱！"})
    submit = SubmitField('注册')

class ForgetPassword(FlaskForm):
    email = StringField('email', validators=[DataRequired(message='不能为空')],  render_kw={'placeholder': "请输入你的邮箱！"})
    number = PasswordField("password", render_kw={'placeholder': "请输入验证码！"})
    sent = SubmitField("发送验证码")
    submit = SubmitField("立即验证")


class NewPassword(FlaskForm):
    password1 = PasswordField('password', validators=[DataRequired(), Length(6, 6, message="密码位数不对！请重新输入")],
                                 render_kw={'placeholder': "请输入您的新密码！"})
    password2 = PasswordField('password', validators=[DataRequired(), EqualTo('password1', "两次密码填写不一样")],
                                 render_kw={'placeholder': "请再次输入您的密码！"})
    submit = SubmitField("确定更改")

class User_edit(FlaskForm):
    aboutme = TextAreaField('message', render_kw={'placeholder': "在此输入个人简介，不能为空！"})
    file = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif'])])
    upload = SubmitField("上传资料")


class WriteForm(FlaskForm):
    title = StringField("write", validators=[DataRequired()], render_kw={'placeholder': "这里输入标题"})
    body = CKEditorField("Body", validators=[DataRequired()])
    sent = SubmitField("发布")

class ReplyForm(FlaskForm):
    body = TextAreaField("Body", validators=[DataRequired()], render_kw={'placeholder': "请在这里发表您的评论"})
    sent = SubmitField("发布")

class ReplyuserForm(FlaskForm):
    body = TextAreaField("Body", validators=[DataRequired()], render_kw={'placeholder': "请在这里发表您的评论"})
    sent = SubmitField("发布")

class SearchForm(FlaskForm):
    message = StringField("搜索", validators=[DataRequired()], render_kw={'placeholder': "输入搜索内容"})
    sent = SubmitField("搜索一下")


class SentForm(FlaskForm):
    body = TextAreaField("Body", validators=[DataRequired()], render_kw={'placeholder': "请在这里发表您的评论"})
    sent = SubmitField("发布")


class Sentlivelife(FlaskForm):
    body = TextAreaField("Body", validators=[DataRequired()], render_kw={'placeholder': "请在这里发表您的感言"})
    sent = SubmitField("发布")


