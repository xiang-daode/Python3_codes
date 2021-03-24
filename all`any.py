# 在这里写上你的代码 :-)

# 这些都是假: '',False,0,(),[],{}
# all()："有‘假’为False，全‘真’为True，iterable为空是True"
# any()："有‘真’为True，全‘假’为False，iterable为空是False"

a=1,2,3,4,5
print(all(a),any(a))

a=1,2,3,4,5,0
print(all(a),any(a))

a=1,2,3,4,5
print(all(a),any(a))

a='','','','','5','0',0
print(all(a),any(a))

a='',False,0,(),[],{}
print(all(a),any(a))
