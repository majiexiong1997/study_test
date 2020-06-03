x = 3
y = 5


def add_value():
    # 相加
    print(x + y)


def Multiply_value(x, y):
    # 相乘
    z = x * y
    print(z)


def less_value():
    # 相减
    return print(y - x)


def except_value(x, y):
    # 相除
    z = x / y
    print(z)


if __name__ == '__main__':
    add_value()
    Multiply_value(4, 4)
    less_value()
    except_value(10, 5)
    # 赋值后的无返回值情况
    a = except_value(10, 5)
    print(a)
