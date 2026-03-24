def get_input():
    expr = input('请输入数字，用空格隔开')
    input_list = expr.split()

    return input_list

def is_valid(input_list):
    try:
        if not input_list:
            return None

        [float(num) for num in input_list]
        return True
    except ValueError:
        return False
    

def calc_min(input_list):
    
    mini_num = float(input_list[0])
    
    for num in input_list[1:]:
        if float(num) <= mini_num:
            mini_num = float(num)
            
    # mini_num = min(float(num) for num in input_list[1:])
    
    return mini_num



def main():
    input_list = get_input()
    if not is_valid(input_list):
       print('有特殊字符，请输入数字')
       return
    
    result = calc_min(input_list)
    if result is None:
        print('为输入任何数字')
    else:
        print('最小的数字是：', result)
        
if __name__ == '__main__':
    main()