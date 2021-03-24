# 在这里写上你的代码 :-)


# 内存读取:=============================================
x = memoryview(bytes(3))	# 查看内存 memoryview	
print(x) #返回内存地址: <memory at 0x000001FF4D3D5F48>

x = memoryview(b'8,7,6,5')	# 查看内存 memoryview	
print(x.tobytes()) #返回: b'8,7,6,5'


x= memoryview(bytearray("abcefg", 'utf-8'))
print(x,x[2],x[-2],x[1:5],x[1:5].tobytes())# 注意下标用法
# <memory at 0x000001FF4D62C048> 99 102 <memory at 0x000001FF4D3D5F48> b'bcef'

print(x.tobytes()) # b'abcefg'
