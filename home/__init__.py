#-*-coding:utf-8-*-
# 刘文豪
# 大帅哥
from flask import Blueprint

home = Blueprint('homeapp', __name__)

from . import view