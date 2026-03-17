import copy


def calc_even_num(input_list, charter):
    """
    统计列表中某个数字出现的次数

    参数:
        input_list: 包含数字字符串的列表
        charter: 需要统计个数的目标数字

    返回:
        int: 目标数字在列表中出现的次数
    """
    temp_list = copy.deepcopy(input_list)

    count = 0
    for item in temp_list:
        if int(item) == int(charter):
            count += 1

    return count


def main():
    """
    程序主入口，获取用户输入并输出指定数字在列表中出现的次数
    """
    expr = input('请输入列表')
    charter = input('请输入需要统计个数的数字')

    input_list = expr.split()

    result = calc_even_num(input_list, charter)

    print('输入的列表中总共有', result, '个', charter)


if __name__ == '__main__':
    main()