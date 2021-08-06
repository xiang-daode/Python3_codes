#list的排序（正序与倒序）
#中文按内码排序，其余按ASCII码排序
x  = [ '一','鸡','鸭','猫','狗','蟋','蟀','蟒','pig','monkey','cat','135','137','0052','3537']
y  = sorted (x)
print(x)
print(y)
y2  =  sorted (x,reverse=True)
print(y2)

