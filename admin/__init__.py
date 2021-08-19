#-*-coding:utf-8-*-
# 刘文豪
# 大帅哥
from flask import Blueprint

admin = Blueprint('adminapp', __name__)

from . import view