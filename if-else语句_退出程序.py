# 在这里写上你的代码 :-)
import sys

age = int( input("请输入你的年龄：") )
if age < 18 :
    print("警告：你还未成年，不能使用该软件！")
    print("未成年人应该好好学习，多多学习，报效祖国。")
    sys.exit()
else:
    print("你已经成年，可以使用该软件。")
    print("时间宝贵，请不要在该软件上浪费太多时间。")
print("软件正在使用中...")



