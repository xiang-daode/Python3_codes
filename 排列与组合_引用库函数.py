# 在这里写上你的代码 :-)
import itertools

# 输出组合结果,---组合是不考虑顺序的:
a1=list(itertools.combinations([1,2,3,4],3))
print(len(a1),a1)
a2=list(itertools.combinations(["A","B","C","D","E"],3))
print(len(a2),a2)

#  输出排列结果,---排列是考虑顺序的:
a1=list(itertools.permutations([1,2,3,4],2))
print(len(a1),a1)
a2=list(itertools.permutations(["A","B","C"],3))
print(len(a2),a2)
