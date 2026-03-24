def get_square(num):
    # return num * num
    # return pow(num, 2)
    return num ** 2

def main():
    expr = input('请输入需要平方的数字：')
    value = int(expr)
    
    result = get_square(value)
    
    print('平方值为：', result)
    
if __name__ == '__main__':
    main()