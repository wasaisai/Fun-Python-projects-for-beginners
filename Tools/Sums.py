
def sum(expr):
    num_list = expr.split()
    sums = float(num_list[0])
    
    for item in num_list[1:]:
        sums +=  float(item)
    
    return sums

def is_valid(expr):

    try:
        valid_expr = expr.split()

        if len(valid_expr) < 2:
            print('请最少输入两个数字')
            return False
        
        # 遍历数组，判断是否是数字类型，若不是，则被捕获到，提示非法字符
        for item in valid_expr:
            float(item)
        
        return True
        
    except ValueError:
        print('非法字符，请输入数字')
        return False
        

def main():
    expr = input('请输入需要计算的数字，空格隔开')

    if is_valid(expr):
        sum(expr)
    else:
        expr = input('请输入需要计算的数字，空格隔开')
        sum(expr)
    
    print('您输入的数字之和为：', sum(expr))  
    

main()