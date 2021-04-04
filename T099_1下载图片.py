# 在这里写上你的代码 :-)
    #保存图片：如果是下载保存图片之类的数据的，注意用'wb'的方式写入：
import requests


r = requests.get('https://www.baidu.com/img/bd_logo1.png')
img = r.content
with open('baidu.png','wb') as f:
    f.write(img)


