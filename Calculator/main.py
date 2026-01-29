import calc
import sys
import gui

def run_cli():
    if len(sys.argv) > 1:
        expr = sys.argv[1]
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

#选择运行模式
def choice_mode():
    print("请选择运行模式：")
    print("1. 命令行（CLI）")
    print("2. 图形界面（GUI）")

    choice = input("请输入 1 或 2：").strip()
    return choice
    

#负责主要流程，  
def main():
    print("\n=== 简易计算器 ===\n")
   
    choice = choice_mode()
    
    if choice == "1":
        run_cli()
    elif choice == "2":
        gui.run_gui()
        

#调用函数
if __name__ == "__main__":
    main()
    
    


