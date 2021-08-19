#encoding:utf-8
# 刘文豪
# 大帅哥
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_dropzone import Dropzone
mail = Mail()  # 实例化对象邮件对象

db = SQLAlchemy()  # 实例化对象数据库

dropzone = Dropzone()




