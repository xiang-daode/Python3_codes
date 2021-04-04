# 在这里写上你的代码 :-)
def enCode(string):
    '''
    这是加密测试,用的是混合运算:异或位运算及加法运算
    ----By daode1212,2021-03-28    '''
    newStr=''
    codes=[]
    for i in range(len(string)):
       m=string[i]
       N0=ord(m)
       N1=(N0^0x3056)+0x1234
       si=chr(N1)
       newStr+=si
       codes.append(N1)
    return [newStr,codes]

# 在这里写上你的代码 :-)
def deCode(string):
    '''
    这是解密测试,用的是逆运算
    ----By daode1212, 2021-03-28    '''
    newStr=''
    for i in range(len(string)):
       m=string[i]
       N0=ord(m)
       N1=(N0-0x1234)^0x3056
       si=chr(N1)
       newStr+=si
    return newStr

print(enCode.__doc__)
s0=enCode('批量生产企业家地下研究所_65536室')
print(s0[0])
print("密电码如下:\n",s0[1])


print(deCode.__doc__)
print(deCode('摣돍坽鄥醋邀縔禚邑婶屔摊䈽䊔䊗䊗䊙䊔縦'))

