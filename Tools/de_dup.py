from copy import deepcopy

def func_de_dup(arr):
    arr_copy = deepcopy(arr)
    
    unique_list = set()
    
    for num in arr_copy:
        unique_list.add(num)
        
    return unique_list
    

def main():
    expr = input('请输入列表，以空格隔开：') 
    input_list = [int(i) for i in expr.split()]
    result = func_de_dup(input_list)
    
    print('去重结果是：', result)
    
    
if __name__ == '__main__':
    main()
    