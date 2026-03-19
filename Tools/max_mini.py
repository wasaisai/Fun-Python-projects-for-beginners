def calc_max(input_list):
    """
    计算列表中的最大值和最小值

    参数:
        input_list: 包含数字的列表

    返回:
        tuple: (最大值, 最小值)
    """
    max_value = input_list[0]

    min_value = input_list[0]

    for item in input_list[1:]:
        if item > max_value:
            max_value = item

        if item < min_value:
            min_value = item

    return max_value, min_value


def main():
    """
    程序主入口，获取用户输入并打印最大值和最小值
    """
    expr = input('请输入需要查找最大值和最小值的数字，用空格隔开')

    input_list = [int(num) for num in expr.split()]

    max_value, min_value = calc_max(input_list)

    print('输入的最大值为：', max_value)
    print('输入的最小值为：', min_value)


if __name__ == '__main__':
    main()
