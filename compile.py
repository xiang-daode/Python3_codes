# 在这里写上你的代码 :-)

# 单一名句用exel:
x = compile('print(12345679*18)', 'test', 'eval')
exec(x)

# 多行语句用exec:
x = compile('''
v=3*3+4*4
u=5*5
w=65536**(1/16)
print(v,u,w)
''',
'myCode', 'exec')
exec(x)


