# 在这里写上你的代码 :-)

# 内码与字节:===[在加密,解密,遥控,通讯中常用]====
x = b"Hello"	# 字节型 bytes	
print(x)  # b'Hello'

x = bytes(4)	# 4个不可修改的,空的字节型数组 byte	
print(x) #  b'\x00\x00\x00\x00'

x = bytes("项,道,德","cp936")	# 以拼音为序, 3个不可修改字节型数组 byte	
print(1,x) #  1 b'\xcf\xee,\xb5\xc0,\xb5\xc2'

x = bytearray(4)	# 4个可修改的,空字节型数组 bytearray	
print(x)#  bytearray(b'\x00\x00\x00\x00')

x ='项,道,德'.encode('gbk') # 以拼音为序, 3个可修改字节型数组 bytearray	
print(2,x) # 2 b'\xcf\xee,\xb5\xc0,\xb5\xc2'

x = bytearray("项 道 德","UTF8")	# 3个可修改字节型数组 bytearray	
print(3,x) # 3 bytearray(b'\xe9\xa1\xb9 \xe9\x81\x93 \xe5\xbe\xb7')

x = ascii("项 道 德")	# 3个可修改字节型数组 bytearray	
print(4,x)  # 4 '\u9879 \u9053 \u5fb7'

# ord()返回对应的 ASCII 数值，或者 Unicode 数值:
x =   ord("项"), ord("道"),ord("德")	# 3个可修改字节型数组 bytearray	
print(5,x) # 5 (39033, 36947, 24503)

x =  hex(ord("项")), hex(ord("道")),hex(ord("德"))	# 3个可修改字节型数组 bytearray	
print(6,x) # 6 ('0x9879', '0x9053', '0x5fb7')

print(bin(ord("项")), bin(ord("道")),bin(ord("德")))
# 0b1001100001111001 0b1001000001010011 0b101111110110111
