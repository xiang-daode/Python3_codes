# 在这里写上你的代码 :-)
'''
题目022：两个乒乓球队进行比赛，各出三人。
甲队为a,b,c三人，乙队为x,y,z三人。
已抽签决定比赛名单。有人向队员打听比赛的名单。
a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
'''

def tm022():
    '''
    【个人备注】：关键是将抽象化，将问题抽象成代码方式。
    是用排列组合函数，列出方案，然后排除。
    而官方解答里面有一个纯粹的for循环加if的求解方式，
    更抽象一些，用了一个很常用固定范式，直接拿来解题了。
    稍微对其抽象的方法注释了一下。
    '''
    import itertools
    jia = ['a','b','c']
    yi = ['x','y','z']
    arr = list(itertools.permutations(yi,3)) # 面对甲队a,b,c时，乙队所有排列 [('x', 'y', 'z'), ('x', 'z', 'y'), ('y', 'x', 'z'), ('y', 'z', 'x'), ('z', 'x', 'y'), ('z', 'y', 'x')]
    arr = [[jia[i]+a[i] for i in range(3)] for a in arr] #将a,b,c写上，得到所有对阵组合 [['ax', 'by', 'cz'], ['ax', 'bz', 'cy'], ['ay', 'bx', 'cz'], ['ay', 'bz', 'cx'], ['az', 'bx', 'cy'], ['az', 'by', 'cx']]
    for i in arr:
        if 'ax' in i:
            pass
        elif 'cx' in i or 'cz' in i:
            pass
        else:
            print(i) # 得到 ['az', 'bx', 'cy']

tm022()
