import sys
import utilies


MODE_FILE = 'mode.txt'

def save_mode(mode):
    with open(MODE_FILE, 'w', encoding="utf-8") as f:
        f.write(mode)
    
    
def load_save():
    try:
        with open(MODE_FILE, "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def get_load_from_argv():
    if "--gui" in sys.argv:
        return "gui"
    if "--cli" in sys.argv:
        return "cli"
    
    return None

#选择运行模式
def choice_mode():
    
    cli_mode, expr = utilies.prase_argv()
    
    #命令行参数：--cli
    if cli_mode:
        choice = cli_mode
        return choice
        
    # 用户上次选择的模式
    last_mode = load_save()
    
    if last_mode:
        print(f"上次使用的是 {last_mode}")
        use_last = input("是否继续使用？(y/n)").strip().lower()
        if use_last == "y":
            return last_mode
    
    print("请选择运行模式：")
    print("1. 命令行(CLI)")
    print("2. 图形界面(GUI)")

    choice = input("请输入 1 或 2:").strip()
    
    return "cli" if choice == "1" else "gui" 
    