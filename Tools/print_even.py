def main():
    """
    生成并打印 1 到 100 之间的所有偶数

    返回:
        list: 包含 1 到 100 之间所有偶数的列表
    """
    result = []

    count = 100

    i = 1

    while i <= count:
        if i % 2 == 0:
            result.append(i)
        i += 1

    return result


if __name__ == '__main__':
    even_list = main()
    print(even_list)
