def stats(expr, char):
    count = 0
    
    for item in expr:
        if item == char:
            count += 1
    
    return count

def is_valid(input_str):
    
    expr_list = input_str.split()
    char = expr_list[1]
    expr = expr_list[0]
    
    if len(expr_list) != 2:
        print('无效输入，请重新输入')
        return False
    elif not expr.isalnum():
        print('仅支持输入字母和数字，请重新输入')
        return False
    elif not char.isalnum():
        print('请仅输入字母或者数字')
        return False
    else:
        return True
      
    
def get_input_str():
    exprs = input('请输入字符串以及需要统计的字符，用空格隔开')
    
    char = exprs.split()[1]
    expr = exprs.split()[0]
    
    return expr, char

def main():
    
    expr, char = get_input_str()
    
    if not is_valid(get_input_str()):
        expr, char = get_input_str()    
    
    total_sum = stats(expr, char)
    
    print('字符',char,'总共出现了',total_sum, '次')
    
    
main()