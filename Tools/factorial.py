def factorial(num):
    """
    计算给定数字的阶乘

    参数:
        num: 需要计算阶乘的整数

    返回:
        int: 阶乘结果，如果输入为负数则返回 None
    """
    if num < 0:
        return None
    
    result = 1
    i = 1
    while i <= num:
        result = i * result
        i += 1
        
    return result
    

def main():
    """
    程序主入口，获取用户输入并计算阶乘
    """
    num = int(input('请输入需要计算阶乘的数字'))
    result = factorial(num)
    
    if result == None:
        print('负数没有阶乘')
    else:
        print(num, '的阶乘是：', result)
    
    
main()