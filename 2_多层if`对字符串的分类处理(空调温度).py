#=== 多层if,对浮点数的分类处理 =====
x=float(input("室内温度是?"))
# ....5度....15度....25度......
if x>25:
    print('制冷器上电')
elif x>=15:
    print('自然风进入')
elif x>=5:
    print('制热器上半电')
else:
    print('制热器上全电 ')
