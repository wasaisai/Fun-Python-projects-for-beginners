# def to_uppercase(expr):
#     return expr.upper

def to_uppercase(expr):
    """
    将字符串中的小写字母转换为大写字母

    参数:
        expr: 待转换的字符串

    返回:
        str: 转换后的字符串，小写字母变为大写，其他字符保持不变
    """
    result = []

    for s in expr:
        if 'a' <= s <= 'z':
            result.append(chr(ord(s) - 32))
        else:
            result.append(s)

    return ''.join(result)


def main():
    """
    程序主入口，获取用户输入并输出转换为大写后的字符串
    """
    expr = input('请输入需要转换为大写的字符串')

    is_uppercase = to_uppercase(expr)

    print('转换后的字符串是：', is_uppercase)


if __name__ == '__main__':
    main()