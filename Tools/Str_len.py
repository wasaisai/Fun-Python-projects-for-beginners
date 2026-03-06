
def calc_for(expr):
    count = 0
    valid_expr =  expr.replace(' ', '')
    for item in valid_expr:
        count += 1
    
    return count


def calc_while(expr):
    count = 0
    i = 0
    while i < len(expr):
        count += 1
        i +=1 
    
    return count



def main():
    expr = input('请输入')
    print('您输入的字符串长度是：', calc_for(expr))
    


main()