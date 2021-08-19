#-*-coding:utf-8-*-
# 刘文豪
# 大帅哥
import requests
from bs4 import BeautifulSoup

def getHtml(url, cssPath):  # 获取HTML页面信息
    response = requests.get(url)
    response.encoding = "utf8"
    Htlmtext = response.text
    soup = BeautifulSoup(Htlmtext, "lxml")
    data = soup.select(cssPath)
    return data


url = "https://www.zhihu.com/special/19681091"
cssPath = "body"
print(getHtml(url, cssPath))