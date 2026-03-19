# 方案一：先转小写再统计（适合初学者理解）
# def find_vowel(expr):
#     exprs = expr.lower()
#
#     vowel_str = 'aeiou'
#
#     count = 0
#
#     for item in exprs:
#         if item in vowel_str:
#             count += 1
#
#     return count


def find_vowel(expr):
    """
    统计字符串中元音字母的数量（不区分大小写）

    参数:
        expr: 待统计的字符串

    返回:
        int: 字符串中元音字母的总数量
    """
    vowel_str = set('aeiouAEIOU')
    count = 0

    for s in expr:
        if s in vowel_str:
            count += 1

    return count


def main():
    """
    程序主入口，获取用户输入并打印元音字母数量
    """
    expr = input('请输入字符串')

    result = find_vowel(expr)

    print('总共输入了', result, '个元音字母')


if __name__ == '__main__':
    main()
