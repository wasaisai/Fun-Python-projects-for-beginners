# def trim_space(expr):
#     return expr.strip()

def strip_space(expr):
    """
    去除字符串两端的空白字符

    参数:
        expr: 待处理的字符串

    返回:
        str: 去除两端空白字符后的字符串
    """
    whitespace = {
        ' ', '\t', '\n', '\r', '\f', '\v'
    }
    start = 0
    while start < len(expr) and expr[start] in whitespace:
        start += 1

    end = len(expr) - 1
    while end >= start and expr[end] in whitespace:
        end -= 1

    return expr[start:end + 1]


def main():
    """
    程序主入口，获取用户输入并输出去除两端空白后的字符串
    """
    expr = input('请输入字符串')
    print(strip_space(expr))


if __name__ == '__main__':
    main()
    
