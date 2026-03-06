
      
def is_even(num) :
    if num % 2 == 0:
        return True
    else:
        return False
    
def parity(num):
    if is_even(num) :
        print('是偶数')
    else:
        print('是奇数')
  
num = int(input('请输入需要计算的数字'))

parity(num)