#encoding:utf-8
# 刘文豪
# 大帅哥
# 该文件存放数据库配置项
import os
from datetime import timedelta
USERNAME = 'blog'
PASSWORD = '196811'
HOST = '118.31.188.167'
PORT = '3306'
DATABASE = 'blog'

DB_URL = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOST, PORT, DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URL

# 动态追踪修改设置，如未设置只会提示警告
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 查询时会显示原始sql语句
SQLALCHEMY_ECHO = True


SECRET_KEY = os.urandom(24)  # 生成密钥
PERMANENT_SESSION_LIFETIME = timedelta(days=0.5)  # 设置为半天

CSRF_ENABLED = True  # 开启CSRF保护


# 发送者邮箱的服务器地址
MAIL_SERVER = "smtp.qq.com"

# MAIL_USE_TLS:端口号587
# MAIL_USE_SSL:端口号465
# QQ邮箱不支持非加密方式发送邮件
MAIL_PORT = 587
MAIL_USE_TLS = True
# MAIL_USE_SSL = False
MAIL_USERNAME = "3513008618@qq.com"  # 发送账户的邮箱
MAIL_PASSWORD = "fcixtiuwzzzbdbfe"  # 连接密码
MAIL_DEFAULT_SENDER = "3513008618@qq.com"  # 发送账户的邮箱

DROPZONE_ALLOWER_FILE_TYPR = 'image, .jpg, .png'  # 只允许图片上传
DROPZONE_MAX_FILE_SIZE = 8  # 最大体积
DROPZONE_MAX_FILES = 3  # 最大数量
DROPZONE_ENABLE_CSRF = True








