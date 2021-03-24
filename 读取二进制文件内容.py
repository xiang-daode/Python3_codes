'''
使用二进制数据记录格式

struct 模块提供了 pack() 和 unpack() 函数，
用于处理不定长度的二进制记录格式。
下面的例子展示了在不使用 zipfile 模块的情况下，
如何循环遍历一个 ZIP 文件的所有头信息。
Pack 代码 "H" 和 "I" 分别代表两字节和四字节无符号整数。
"<" 代表它们是标准尺寸的小端字节序:


'''

import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to the next header
