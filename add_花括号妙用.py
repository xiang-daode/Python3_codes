
def add(a, b):
    return a + b


if __name__ == "__main__":
    a = 5
    b = 6
    # 当字符串前面用格式化标志f,字符串内部用了花括号时,可视作代码[具执行功能]:
    print(f"The sum of {a} + {b} is {add(a, b)}")
    print(f'The  {a}*{b} is {a*b}')
