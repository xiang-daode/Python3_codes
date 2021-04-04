# 在这里写上你的代码 :-)
import itertools

def tm001_1():
    '''
    【备注】：引用python自带排列组合模块itertools，可以直接调用。
     排列计算公式: A(4,3) = (4)!/(4-3)! = (4*3*2*1)/1 = 24
    '''

    #四张卡片抽出3张的所有排列是:
    temp_arr = list(itertools.permutations([1, 2, 3, 4], 3))
    arr = [100*t[0]+10*t[1]+t[2] for t in temp_arr]
    print(len(arr),arr)

# 查看一下"temp_arr = list(itertools.permutations([1, 2, 3, 4], 3))"的输出:
#print(tuple(itertools.permutations((1,3,5,7), 3)),"---元组中嵌套元组")
#print(set(itertools.permutations((2,4,6,8), 3)),"---集合中嵌套元组")
print(list(itertools.permutations([1,3,5,7], 3)),"---列表中嵌套元组")

#执行自定义函数:
tm001_1()
