def calc_sum(input_list):
    """
    计算列表中所有数字的总和

    参数:
        input_list: 包含数字字符串的列表

    返回:
        int: 列表中所有数字的总和
    """
    result = int(input_list[0])
    for item in input_list[1:]:
        result = result + int(item)

    return result


def main():
    """
    程序主入口，获取用户输入并打印所有数字的总和
    """
    expr = input('请输入需要求和的数字，用空格隔开')
    input_list = expr.split()

    sum_value = calc_sum(input_list)
    print('你输入的数字的和为：', sum_value)


if __name__ == '__main__':
    main()
