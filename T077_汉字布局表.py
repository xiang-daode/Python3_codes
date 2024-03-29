# 在这里写上你的代码 :-)
"""
题目077_汉字布局表
"""


def tm077():
    """
    【备注】：
    """
    l = [1, 2, 3, 4, 5]
    for i in l:
        s = chr(0x4E00 + i)
        print(s, end="")
    print()
    for i in range(5, 150):
        s = chr(0x4E00 + i)
        print(s, end="")
    print()
    for i in range(0x9FA6, 0x9FEF):
        s = chr(i)
        print(s, end="")
    print()
    for i in range(0x2B740, 0x2B81D):
        s = chr(i)
        print(s, end="")
    print()

tm077()

"""
字符集	字数	Unicode 编码
基本汉字	20902字	4E00-9FA5
基本汉字补充	74字	9FA6-9FEF
扩展A	6582字	3400-4DB5
扩展B	42711字	20000-2A6D6
扩展C	4149字	2A700-2B734
扩展D	222字	2B740-2B81D
扩展E	5762字	2B820-2CEA1
扩展F	7473字	2CEB0-2EBE0
扩展G	4939字	30000-3134A
康熙部首	214字	2F00-2FD5
部首扩展	115字	2E80-2EF3
兼容汉字	477字	F900-FAD9
兼容扩展	542字	2F800-2FA1D
PUA(GBK)部件	81字	E815-E86F
部件扩展	452字	E400-E5E8
PUA增补	207字	E600-E6CF
汉字笔画	36字	    31C0-31E3
汉字结构	12字	    2FF0-2FFB
汉语注音	43字	    3105-312F
注音扩展	22字	    31A0-31BA
〇	    1字	    3007
"""
