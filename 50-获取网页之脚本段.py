# -*- coding:utf-8 -*-
''' python用于爬虫的库为urllib:
    urllib.request 用于打开和读取URL,
    urllib.error 用于处理前面request引起的异常,
    urllib.parse 用于解析URL,
    urllib.robotparser 用于解析robots.txt文件
'''

import urllib.request
import urllib.error
import urllib.parse
import urllib.robotparser
import json
from urllib.request import urlopen

#导入urlopen函数
#读取网页内容，如果网页中又中文要用“utf-8”解码
html = urlopen(
    "https://mp.csdn.net/postedit"
).read().decode('utf-8')

a=html.split("<script")
k=0
for x in a:
    if k>0:
        b=x.split("script>")
        print('[script---',b[0],'---script]')
    k=k+1












