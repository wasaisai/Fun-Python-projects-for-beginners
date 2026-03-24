
def str_add(expr):
    
    return "-".join(expr)


def main():
    expr = input('请输入需要处理的字符串')
    
    result = str_add(expr)
    
    print(result)
   
   
if __name__ == '__main__':
    main()