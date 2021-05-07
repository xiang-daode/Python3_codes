#注释部分可以调试完成后再添加,  列表与下标
#列表对象(list)与下标:
a=["cat","fox","pig","dog","bee","ant","cow"]
print(a[0])#cat
print(a[-1])#输出: cow
print(a[0:3])#输出: ['cat', 'fox', 'pig']
print(a[-1:-5:-1])#输出: ['cow', 'ant', 'bee', 'dog']
print(a[3:])#输出: ['dog', 'bee', 'ant', 'cow']
print(a[:3])#输出: ['cat', 'fox', 'pig']
print(a[::2])#输出: ['cat', 'pig', 'bee', 'cow']
print(a[::-2])#输出: ['cow', 'bee', 'pig', 'cat']
print(a[::-1]) #逆序输出各元素

a="12345abcdef"
print(a[::-1]) #逆序输出:fedcba54321

#注,英语表示了:[“猫”，“狐狸”，“猪”，“狗”，“蜜蜂”，“蚂蚁”，“牛”]
