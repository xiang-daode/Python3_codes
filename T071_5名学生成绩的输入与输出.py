# 在这里写上你的代码 :-)
'''
题目071：编写input()和output()函数输入，输出5个学生的数据记录。
'''
def tm071():
    '''
    【个人备注】：用字典类型随便写写
    '''
    def inp(data):
        name = input('输入学生姓名：')
        score = input('输入学生成绩：')
        data[name]=score
        print('成功录入')
        return data

    def outp(data):
        name = input('输入学生姓名：')
        print('该学生的成绩是：',data.get(name))
        return data

    if __name__ == '__main__':
        data = {}
        while 1:
            a = input('输入/输出学生成绩(i/o)：')
            if a=='i':
                data = inp(data)
            elif a=='o':
                data = outp(data)
            else:
                print('输入值不对')

tm071()
