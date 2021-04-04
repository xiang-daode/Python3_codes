#自定义函数-1,输入参数属元组,输出是参数集合:
def print_hi(name):
    print(f'Hi,大佬 !, {name}')
    # or print('Hi,大佬 !', {name})
#调用print_hi:
print_hi({'Python !',"I am  a new programer."})

#自定义函数-2,输入参数是集合,输出参数用元组:
def print_mmss(name):
    print(f'Max,Min,Sum,Sorted is:,{max(name),min(name),sum(name),sorted(name)}')
    # or print('Max,Min,Sum,Sorted is:',{max(name),min(name),sum(name),sorted(name)})
#调用print_mmss:
print_mmss({44, 33, 55, 77})