def find_second_max(arr):
    n = len(arr)
    first = float('-inf')
    second = float('-inf')
        
    for i in range(n):
        if arr[i] > first:
            second = first
            first = arr[i]
            
        elif arr[i] > second and arr[i] < first:
            second = arr[i]

    return second if second != float('-inf') else None
                
        
    


def main():
    expr = input('请输入列表，以空格隔开：')
    
    input_list = [int(i) for i in expr.split()]
    
    result = find_second_max(input_list)
    
    print('第二大数字是：', result)
    

if __name__ == '__main__':
    main()