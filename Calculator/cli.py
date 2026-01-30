import calc
import utilies 


def run_cli():

    mode, expr = utilies.prase_argv()

    if expr:
        result = calc.calculate_express(expr)
        print("结果是：", result)
        return
    
  
    while True:
        expr = input("请输入表达式（如 3 + 5），或 q 退出：")
        
        if expr == "q":
            print("退出计算器 👋")
            break 
        
        result = calc.calculate_express(expr)
        print("结果是：", result)
