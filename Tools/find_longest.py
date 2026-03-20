def func_find_longest(input_list):
    """
    找出列表中最长的字符串

    参数:
        input_list: 包含字符串的列表

    返回:
        str: 列表中最长的字符串
    """
    longest_str = input_list[0]

    for item in input_list:
        if len(item) >= len(longest_str):
            longest_str = item

    return longest_str


def main():
    """
    程序主入口，接收用户输入并输出最长字符串
    """
    expr = input('请输入需要查找的字符串列表，用空格隔开')

    input_list = expr.split()

    result = func_find_longest(input_list)

    print('最长的字符串是：', result)


if __name__ == '__main__':
    main()
