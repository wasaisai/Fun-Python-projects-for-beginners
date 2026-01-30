import cli
import gui
import mode

#负责主要流程，  
def main():
    print("\n=== 简易计算器 ===\n")
    
    
    
    choice = mode.get_load_from_argv()
    
    if not choice:
        choice = mode.choice_mode()
        
    mode.save_mode(choice)
   
    if choice == "cli":
        cli.run_cli()
    elif choice == "gui":
        gui.run_gui()
    else:
        print("❌未知错误")
        

#调用函数
if __name__ == "__main__":
    main()
    
    


