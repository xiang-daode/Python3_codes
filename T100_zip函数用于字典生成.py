# 在这里写上你的代码 :-)
'''
题目100c：用zip函数生成字典。
'''

def tm100c():
    l = ['今天','爷爷','相当','开心']
    d=dict(zip(range(len(l)),l)) #列表转为字典
    print(d)
    print(d[1],d[0],d[2],d[3])#用键访问值
    print(''.join(list(d.values()))) #将字典各值串接起来

tm100c()
