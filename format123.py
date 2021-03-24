# 在这里写上你的代码 :-)
#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "Bill", age = 63)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("Bill",63)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("Bill",63)
print(txt1,txt2,txt3)

