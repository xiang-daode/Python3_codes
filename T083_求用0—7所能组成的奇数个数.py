# 在这里写上你的代码 :-)
'''
题目083：求0—7所能组成的奇数个数。
'''
def tm083():
    '''
    【个人备注】：没说组成几位数或是否重复使用。假设1-8位都可以，且不能重复使用。
    直接用排列函数，累加然后去重，就得到答案了。
    '''
    s = [i for i in '01234567']
    import itertools #有排列与组合函数
    arr = []
    for i in range(1,9):
        a = list(itertools.permutations(s,i))       # 长度1-8左右排列
        l = list(map(lambda x:int(''.join(x)),a))   # 整理成数字形式（避免出现02这种情况，02实际上就是2）
        arr+=l
        print(i,len(l))
        arr1 = set(arr)                                 # 去重复的
    arr2 = list(filter(lambda x:x%2==1,arr1))       # 只留奇数
    print(len(arr),len(arr1),len(arr2))             # 答案是46972

tm083()
