def calc_palindrome(expr):
    """
    判断字符串是否为回文字符串

    参数:
        expr: 待判断的字符串

    返回:
        bool: 如果是回文字符串返回 True，否则返回 False
    """
    # 方案1：双指针法（当前使用）
    # 优点：直观易懂，适合初学者理解回文的判断逻辑
    # 缺点：代码稍长
    start = 0
    end = len(expr) - 1

    while start < end:
        if expr[start] != expr[end]:
            return False
        start += 1
        end -= 1

    return True

    # 方案2：字符串反转（最简单）
    # 优点：代码简洁，一行实现
    # 缺点：需要创建新字符串，占用额外内存
    # return expr == expr[::-1]

    # 方案3：使用 reversed() 函数
    # 优点：可读性好，表达清晰
    # 缺点：需要转换为列表比较
    # return list(expr) == list(reversed(expr))


def main():
    """
    程序主入口，获取用户输入并判断是否为回文字符串
    """
    expr = input('请输入字符串')

    result = calc_palindrome(expr)

    if result:
        print('是回文字符串')
    else:
        print('不是回文字符串')


if __name__ == '__main__':
    main()