
def func_add(expr):
    
    return "-".join(expr)


def main():
    expr = input('请输入需要处理的字符串')
    
    result = func_add(expr)
    
    print(result)
    
main()