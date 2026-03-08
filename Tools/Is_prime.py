    
def basic_term(num):
    if num <= 1:
        return False
    elif num in (2, 3):
        return True
    elif num % 2 == 0:
        return False
    else:
        return True
    

def final_term(num):
    root_num = int(num ** 0.5 + 1)
    i = 3
    while i < root_num:
        if num % i == 0:
            return False
        
        i += 2
        
    return True

  
def main():
    number = int(input('请输入需要判断是否为质数的数字'))
    
    if basic_term(number):
        if final_term(number):
            print ('是质数')
        else:
            print('不是质数')
    else:
        print('不是质数')
        
main()