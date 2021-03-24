# 在这里写上你的代码 :-)

#日期与时间
import datetime
dt=datetime.datetime.now()
print("全部信息为:",dt)

s=dt.strftime("%Y-%m-%d %H:%M:%S")
print("当前时间是: ",s)

#可作随机数用的6位整数(类型:字符串,单位:us):
s=dt.utcnow().strftime('%f')
print(s,type(s))
