# Python3.7中,需调用bytes
# 按对应关系转换数字的:
intab = b"0123456789,"
outtab = b"qr#tuvwxy@_"
trantab = bytes.maketrans(intab, outtab)
#测试:
s4 = "1245,5678,2345,9743,2378,1253"
print(s4.translate(trantab)) #输出:r#uv_vwxy_#tuv_@xut_#txy_r#vt

# 按对应关系转换字母的:
inStr = b"abcdefghijklnopqrstuvwxyz0123456789 ,"
ouStr = b"uvlngwxyzopqrsdefabchitjk9054782361-&"
trantab = bytes.maketrans(inStr, ouStr)
# 测试:
s4 = "My name is bigPig, 63 years old, now.".lower() #转换为小写字母,转换为大写是: upper()
print(s4.translate(trantab))#输出:mj-rumg-za-vzxdzx&-24-jgufa-sqn&-rsi.
