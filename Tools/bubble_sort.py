from copy import deepcopy

def bubble_sort(arr):
    n = len(arr)
    arr_copy = deepcopy(arr)

    for i in range(n):
        arr_copy[i] = int(arr_copy[i])
        for j in range(i +1, n - 1 - i):
            arr_copy[j] = int(arr_copy[j])
            if arr_copy[i] > arr_copy[j]:
                temp = arr_copy[j]
                arr_copy[j] = arr_copy[i]
                arr_copy[i] = temp
                
    return arr_copy


def main():
    expr = input('请输入列表，以空格分隔：')
    
    input_list = expr.split()
    
    result = bubble_sort(input_list)
    
    print('排序结果:', result)
    
    
if __name__ == '__main__':
    main()