error_map = {
    1: '请输入最少两个数字',
    2: '非法字符，请重新输入'
}

def is_valid(expr):

    if len(expr) < 2:
        print(error_map.get(1))
        return 1
    
    if expr.isdigit():
        return True
    else:
        print(error_map.get(2))
        return 2
    


def calculate_express(expr):
    input_list = expr.split()
    
    return input_list



def calc_max(input_list):
   
    max_value = int(input_list[0])
    
    for item in input_list[1:]:
        cur_item = int(item)

        if cur_item > max_value:
            max_value = cur_item
    
    return max_value


def main(expr):
    expr_list = calculate_express(expr)
    max_value = calc_max(expr_list)
    print('您输入的最大值是：', max_value)


if __name__ == '__main__':
    expr = input('请输入需要计算最大值的数字列表，用空格隔开: ')

    if is_valid(expr) == 2:
        expr = input('请输入需要计算最大值的数字列表，用空格隔开: ')
        main(expr)
    else:
        main(expr)
