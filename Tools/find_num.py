def find_num(input_list):
    """
    从列表中找出所有大于 10 的数字

    参数:
        input_list: 包含数字字符串的列表

    返回:
        list: 包含所有大于 10 的浮点数的列表
    """
    find_result = []
    for item in input_list:
        if float(item) > 10:
            find_result.append(float(item))

    return find_result


def main():
    """
    程序主入口，获取用户输入并打印大于 10 的数字
    """
    expr = input('请输入数字，用空格隔开')

    input_list = expr.split()

    result = find_num(input_list)

    print('您输入的数字中，大于10的数字有：', result)


if __name__ == '__main__':
    main()
