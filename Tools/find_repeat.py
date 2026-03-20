from collections import Counter


# 方案一：使用 set 查找所有重复元素（适合初学者理解）
# def find_duplicates(expr):
#     seen = set()
#     duplicates = set()
#
#     for item in expr:
#         if item in seen:
#             duplicates.add(item)
#         else:
#             seen.add(item)
#
#     return list(duplicates)


def find_duplicates(expr):
    """
    找出列表中出现次数最多的元素及其出现次数

    参数:
        expr: 待统计的列表

    返回:
        list: 包含一个元组 (元素, 出现次数)，表示出现次数最多的元素
    """
    return Counter(expr).most_common(1)


def main():
    """
    程序主入口，获取用户输入并打印出现次数最多的元素
    """
    expr = input('请输入需要统计的字符, 用空格隔开')

    input_list = expr.split()

    result = find_duplicates(input_list)

    print('结果是：', result)


if __name__ == '__main__':
    main()
