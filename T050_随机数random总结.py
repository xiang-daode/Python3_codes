# 在这里写上你的代码 :-)
'''
题目050：输出一个随机数。
'''
def tm050():
    '''
    【个人备注】：之前学习随机的时候整理的东西，用到时候来找就行了
    '''
    import random

    # 随机数操作
    a=random.random()             # 0.85415370477785668   # 随机一个[0,1)之间的浮点数
    b=random.uniform(0, 100)      # 18.7356606526         # 随机一个[0,100]之间的浮点数
    c=random.randrange(0, 100, 2) # 44                    # 随机一个[0,100)之间的偶数
    d=random.randint(0, 100)      # 22                    # 随机一个[0,100]之间的整数

    # 随机字符操作
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-" # 任意字符串（作为随机字符种子库）
    e=random.choice(seed)             # 'd'               # 随机一个字符
    f=random.sample(seed, 3)          # ['a', 'd', 'b']   # 随机多个字符（字符可重复）
    g=''.join(random.sample(seed,3))  # '^f^'             # 随机指定长度字符串（字符可重复）

    # 列表操作:用打乱产生随机位置
    lt=['玩偶','爱','儿子','卖']
    h=random.shuffle(lt)                                # 列表中的元素打乱
    print(a,b,c,d,e,f,g,lt)

    #随机姓名:
    h1=random.randrange(0x4e00, 0x9fa5) #随机汉字1
    h2=random.randrange(0x4e00, 0x9fa5) #随机汉字2
    print('项'+chr(h1)+chr(h2)) #随机姓名

    #约束到三位小数:
    a,b,c=random.random(),random.random(),random.random()
    print("%.3f,%.3f,%.3f,"%(a,b,c))


tm050()
