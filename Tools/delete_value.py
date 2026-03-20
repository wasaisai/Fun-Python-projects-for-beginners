import copy

def delete_value(input_list, char):
    
    list_value = copy.deepcopy(input_list)
    for item in input_list:
        if item == char:
           list_value.remove(item)
           
    return list_value



def main():
    expr = input('请输入列表')
    char = input('请输入需要删除的值')
    input_list = expr.split()
    
    if char not in input_list:
        print('该字符不在列表内, 请重新输入')
        return
    
    result = delete_value(input_list, char)
    
    print('已删除', char, result)
    
    
main()