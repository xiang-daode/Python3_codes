####################### List基本用法 ###########################

MyList=[3,4,5,6,-3,-2,-1,0,1,2,7,8,9]
print("数据之个数:",len(MyList))
print("最大值:",max(MyList))
print("最小值:",min(MyList))
print("求和:",sum(MyList))

print("8出现次数:",MyList.count('8'))
print("8出现在:",MyList.index(8))

MyList.sort()
print("最小的头四个数:",MyList[0:4])
print("最大的头四个数:",MyList[-1:-5:-1])


MyList.sort(reverse=True)
print("最大的头四个数:",MyList[0:4])
print("最小的头四个数:",MyList[-1:-5:-1])


#############  依赖random库计算  ##############
import random

random.shuffle(MyList)   ##随机打乱MyList
print(MyList)


#############  依赖numpy库计算List  ##############
import numpy as np

#求和:
a_sum = np.sum(MyList)
print("和为：%0.2f" % a_sum)
#求均值:
a_mean = np.mean(MyList)
print("平均值为：%0.2f" % a_mean)
#求方差:
a_var = np.var(MyList)
print("方差为：%0.2f" % a_var)
#求标准差:
a_std = np.std(MyList,ddof=1)
print("标准差为:%0.6f" % a_std)

#################### 用迭代器生成新的列表 #########################
newL=[]
for m in MyList:
    newL.append(m*100)
print("新的列表如下:\n",newL)

##################  将列表中所有元素清空  #######################
MyList.clear()	
print("MyList列表如下:\n",MyList)


##################### 数据的映射(map)与筛选(filter)  ##########################
L1=list(map(lambda x: x/100,newL))
print("重新计算各元素:\n",L1)

L2=list(filter(lambda x: x>300,newL))
print("取出>300的元素:\n",L2)

L3=list(filter(lambda x: x>100 and x<500,newL))
print("在(x>100 and x<500)区间中:\n",L3)

L4=list(filter(lambda x: (x==300 or x==500),newL))
print("找特定的数据:\n",L4)


'''
方法			描述
append()	在列表的末尾添加一个元素
clear()		删除列表中的所有元素
copy()		返回列表的副本
count()		返回具有指定值的元素数量。
extend()	将列表元素（或任何可迭代的元素）添加到当前列表的末尾
index()		返回具有指定值的第一个元素的索引
insert()	在指定位置添加元素
pop()		删除指定位置的元素
remove()	删除具有指定值的项目
reverse()	颠倒列表的顺序
sort()		对列表进行排序

# =================  一些示例  =====================
MyList.pop()    ##弹出最后一个元素
a = MyList.pop(0)  ##弹出下标[0]的元素
MyList.remove('fox') ##指定删除对象的名字
del MyList   ##直接删除整个列表
print(MyList + ['fox'])   ##用连接的方式
MyList.append('fox')
print(MyList)    ##append:追加一个元素到列表尾巴后
extend:拉伸 追加多个元素到列表中
MyList.extend(['pig','dog'])
MyList.insert(1,'xo')  ###在指定下标处[索引位置]插入元素  ##在第二个元素的位置插入ba作为第二个元素
MyList.count('xo') ###统计出现多少个
MyList.index('xo')    ###找到的最小索引值
MyList.index('xo',1,3)   ###从下标[1:3]中查找【第二个元素和第三个元素之间】【不取上限】

MyList = ['alice','Bob','coco','Harry']
MyList.sort() ##按照ASCII排序
MyList.sort(reverse=True) ##按照ASCII倒排序
MyList.sort(key=str.lower)   ###对字符串排序不区分大小写，相当于将所有元素转换为小写，再排序
MyList.sort(key=str.upper)   ###相当于将所有元素转换为大写，再排序
————————————————
MyList= list(range(10))   ##生成0-9，将其转换为列表形式
import random
random.shuffle(MyList)   ##随机打乱MyList
'''
