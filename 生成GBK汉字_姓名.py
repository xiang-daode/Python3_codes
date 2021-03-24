# 在这里写上你的代码 :-)
import random

def Unicode():
    val = random.randint(0x4e00, 0x9fbf)
    return chr(val)

def GBK2312():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xfe)
    val = f'{head:x} {body:x}'
    str = bytes.fromhex(val).decode('gb2312')
    return str

print("========= 子子孙孙之姓名 ==========")
for i in range(8*16):
    if(i % 8==0):
        print('')
    for j in range(2):
        print("项"+GBK2312()+GBK2312(),end=',')

print("\n========= 项道德 撰 ==========")

