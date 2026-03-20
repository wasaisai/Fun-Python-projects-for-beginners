def create_list(char):
    """
    生成从 1 到 char 的整数列表

    参数:
        char: 列表的最大值（整数）

    返回:
        list: 包含从 1 到 char 的整数列表
    """
    i = 1

    count = 1

    result_list = []

    while count <= char:
        result_list.append(i)

        i += 1
        count += 1

    return result_list


def main():
    """
    程序主入口，获取用户输入并打印生成的列表
    """
    char = int(input('请输入需要生成的列表的最大值：'))

    result = create_list(char)

    print('生成的列表：', result)


if __name__ == '__main__':
    main()
