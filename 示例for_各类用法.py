# 在这里写上你的代码 :-)
#for 循环用于迭代序列（即:字符串,区间,列表,元组,集合,字典）
#循环结构是编程中最重要的,也是CPU快速高效处理数据的必经之路

print()
#遍历字符串string:
for m in "123456789":
  print(m,end='_')

print()
#遍历区间(范围)range:
for m in range(1,21,2):
  print(m,end='.')

print()
#遍历列表list:
for m in ['11','22','33','44','55']:
  print(m,end='|')

print()
#遍历元组tuple:
for m in ("fox","pig","cat","dog"):
  print(m,end=',')

print()
#遍历集合set:
for m in {"红","绿","蓝","黑","白"}:
  print(m,end=' ')
print()
#遍历冻结集合frozenset:
for m in frozenset({"红","绿","蓝","黑","白"}):
  print(m,end='+')

print()
#遍历字典dict,由"键-值"对构成的集合,如以身份证为键,或以姓名为键:
d={"红":"FF0000", "绿":"00FF00", "蓝":"0000FF", "黑":"000000", "白":"FFFFFF"}
for m in d:
  #print(m,end='_') #只输出"键"
  print(m,"=0x"+d[m],end=';  ')  # m:键, d[m]:值
