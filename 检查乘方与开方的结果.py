
# 函数以逻辑型数据作返回值:
def perfect_cube(n: int) -> bool:
    """
    乘方与开方并非完全是逆运算,在计算机浮点处理中,有时会出现微小的误差:
    """
    val = n ** (1 / 3)
    n3=val * val * val
    print(n3,end='-->')
    return (n3) == n


if __name__ == "__main__":
    print(perfect_cube(27))
    print(perfect_cube(4))

    print(perfect_cube(125))
    print(perfect_cube(100))
