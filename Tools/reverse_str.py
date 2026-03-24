def reverse(exprs):
    reverse_list = [0] * len(exprs)
        
    i = len(exprs) -1
    index = 0
    
    while i >= 0 and index < len(exprs):
        reverse_list[i] = exprs[index]
        i -= 1
        index += 1
    
    #使用join
    reverse_str = ''.join(reverse_list)
    
    # 使用+
    # for item in reverse_list:
    #     reverse_str = reverse_str + item
        
    return reverse_str

def main():
    expr = input('请输入字符串')
    
    print(reverse(expr))
    
if __name__ == '__main__':
    main()