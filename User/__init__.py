#-*-coding:utf-8-*-
# 刘文豪
# 大帅哥

from flask import Blueprint

user = Blueprint('userapp', __name__)

from . import view