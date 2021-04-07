import zlib
#生成连续汉字
s = b'12,34,56'
c = zlib.crc32(s)
print(c,s)