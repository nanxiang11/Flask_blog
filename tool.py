#-*-coding:utf-8-*-
# 刘文豪
# 大帅哥
from flask import Flask, url_for
import random
class Password:
    a = [64, 83, 33, 102, 98, 57]

    def __init__(self, number):
        self.number = number
        self.s = ''
        self.s2 = ''

    def encryption(self):  # 加密
        self.s = ''
        b = 0

        for i in self.number:
            if b < len(self.number):
                self.s = self.s + chr(int(i) + Password.a[b])
                b = b + 1
        return self.s

    def deciphering(self):  # 解密
        self.s2 = ''
        b = 0
        for i in self.number:
            if b < len(self.number):
                self.s2 = self.s2 + str((ord(i) - Password.a[b]))
                b = b + 1
        return self.s2


class OnlySign:  # 标识类
    def __init__(self):
        self.KU = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    def carry(self):  # 随机6位标识
        b = ''
        for i in range(0, 6):
            b = b + self.KU[random.randint(0, 24)]
        return b


import os
from PIL import Image

def set_img(file, path):
    img = Image.open(file)
    w, h = img.size
    newimg = img.resize((int(w/5), int(h/5)), Image.ANTIALIAS)
    newimg.save(path)


from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random


def validate_picture():
    total = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345789'
    # 图片大小130 x 50
    width = 100
    heighth = 30
    # 先生成一个新图片对象
    im = Image.new('RGB',(width, heighth), 'white')
    # 设置字体
    font = ImageFont.truetype(url_for('static', filename='STSONG.TTF'), 18)
    # 创建draw对象
    draw = ImageDraw.Draw(im)
    str = ''
    # 输出每一个文字
    for item in range(4):
        text = random.choice(total)
        str += text
        draw.text((5+random.randint(4, 7)+20*item, 5+random.randint(3, 7)), text=text, fill='black', font=font)

    # 划几根干扰线
    for num in range(4):
        x1 = random.randint(0, width/2)
        y1 = random.randint(0, heighth/2)
        x2 = random.randint(0, width)
        y2 = random.randint(heighth/2, heighth)
        draw.line(((x1, y1), (x2, y2)), fill='black', width=1)

    # 模糊下,加个帅帅的滤镜～
    im = im.filter(ImageFilter.FIND_EDGES)
    return im, str
