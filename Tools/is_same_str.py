def is_same_str(str01, str02):
    
    str01_len = len(str01)
    str02_len = len(str02)
    
    if str01_len != str02_len:
        return False
    
    n = str01_len
    
    for i in range(n):
        if str01[i] != str02[i]:
            return False
    
    return True


def main():
    expr01 = input('请输入第一个字符串')
    expr02 = input('请输入第二个字符串')
    
    result = is_same_str(expr01, expr02)
    
    if result:
        print('是相同字符串')
    else:
        print('不是相同字符串')
    
    
if __name__ == '__main__':
    main()
    