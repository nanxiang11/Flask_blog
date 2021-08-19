# -*-coding:utf-8-*-
# 刘文豪
# 大帅哥
from flask import flash
from flask_wtf.file import FileAllowed, FileRequired
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, Form, TextAreaField, FileField  ## WTF
from wtforms.validators import DataRequired, Length, EqualTo, Email  ## 验证器属性选项
from flask_ckeditor import CKEditorField


class SentForm(FlaskForm):
    body = TextAreaField("Body", validators=[DataRequired()], render_kw={'placeholder': "请在这里回复私信"})
    Reply = SubmitField("发布")
