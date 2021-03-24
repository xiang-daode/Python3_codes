# 在这里写上你的代码 :-)
# 从二进制数据库文件读取固定宽度的块，直到到达文件的末尾
from functools import partial
with open('id.py', 'rb') as f:
   for block in iter(partial(f.read, 16), b''):
     print(block)# process_block(block)
