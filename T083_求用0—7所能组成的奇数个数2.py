'''
题目083：求0—7所能组成的奇数个数。
'''
def tm083_1():
    '''
    【备注】： 用穷举法验证验证了一下
    '''
    count = 0
    for i in range(76543211):       # 能组成的最大数字也就是76543210了
        s = str(i)                  # 转换成文本形式s
        if '8' in s or '9' in s:    # s中不包含8和9
            continue
        else:
            cs = set([c for c in s])# s中的数字去重，如果去重后和去重前长度一致，说明数字没有重复使用
            if len(s)==len(cs) and s[-1] in '1357': # 各位不重复且是奇数
                count+=1
        if i%100000==0:print(i,count) # 每10万个输出一下结果，避免程序卡死发现不了。
    print(count) # 结果=46972。

tm083_1()
