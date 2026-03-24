case = [
    ' ',
    '1234',
    '23',
    '    '
]

def calc(calc_str):
    
    for item in calc_str:
        str_item = item.replace(' ', '')
        if len(str_item) == 0:
           print('空字符串')   
           return True     
        
def main():
    expr = input('请输入')
    calc(expr)
    
if __name__ == '__main__':
    main()