# 在这里写上你的代码 :-)

n = int( input("24个2连乘,2**24=?,pow(2,24)=? \r\n请输入计算结果："))
if n != 16777216 :
    print("计算结果错误")
else:
    print("计算结果正确!很棒.")
# 该语句不属于if的代码块
print("以后继续努力...")


age = int( input("请输入你的年龄：") )

if age < 16 :
    print("你还未成年，建议在家人陪同下使用该软件！")
    print("如果你已经得到了家长的同意，请忽略以上提示。")

# 该语句不属于if的代码块
print("软件正在使用中...")
