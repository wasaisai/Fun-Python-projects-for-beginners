def concat_list(list_01, list_02):
    """
    合并两个列表并转换元素类型

    参数:
        list_01: 第一个列表
        list_02: 第二个列表

    返回:
        list: 合并后的列表，数字字符串转换为整数，其他保持字符串
    """
    mixed_list = list_01 + list_02

    clean_list = []
    for item in mixed_list:
        try:
            clean_list.append(int(item))
        except ValueError:
            clean_list.append(item)

    return clean_list


def main():
    """
    程序主入口，获取用户输入的两个列表并输出合并后的结果
    """
    expr01 = input('请输入需要合并的第一个列表，每个数字之间用空格隔开：')
    expr02 = input('请输入需要合并的第二个列表，每个数字之间用空格隔开：')

    list_01 = expr01.split()
    list_02 = expr02.split()

    print('合并后的列表是：', concat_list(list_01, list_02))


if __name__ == '__main__':
    main()