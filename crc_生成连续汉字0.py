import zlib
#生成连续汉字
s = b'12,34,56'
for i in range(99):
    c = zlib.crc32(s)
    ch=chr(0x4e00+c % (0x9fa5-0x4e00))
    print(ch,end='')
    s=ord(ch).to_bytes(2, byteorder='big')
print('\n-----------------\n')

#生成连续汉字
s = b'3056'
for i in range(99):
    c = zlib.crc32(s)
    ch=chr(0x4e00+c % (0x9fa5-0x4e00))
    print(ch,end='')
    s=ord(ch).to_bytes(2, byteorder='big')
print()