#===============  设计空调电脑板  ===================
'''
a=float(input("输入当前温度:"))

if a<=15:
     print(a ,'开启制热' )   
elif a>=15 and a<25:
    print(a ,'开启自然风')
else:
    print(a ,'开启制冷')
'''

#===============  军方决策  ===================
a=input("输入当前敌人的类别{空军,海军,陆军}:")

if a=='陆军':
     print('陆军回击' )   
elif a=='海军':
    print(' 海军回击')
elif a=='空军':
    print('空军回击')
elif a=='陆军,海军' or a=='海军,陆军' :
    print('导弹军1回击')
elif  a=='空军,海军' or a=='海军,空军' : 
    print('导弹军2回击')
elif ('陆军'in a) and ('海军'in a) and ('空军' in a):
    print('太空军3回击')
else:
    print('全民皆兵')    
