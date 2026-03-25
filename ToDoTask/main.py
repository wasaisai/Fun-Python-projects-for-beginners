import os

def add_task(file_name):
    expr = input('请输入需要添加的待办事项, 若多项请用空格隔开')
    try:
        with open(file_name, 'a', encoding='utf-8') as f:
            
            f.writelines(f"{expr}")
    except FileExistsError:
        print('写入文件失败')

def check_task(file_name):

        try:
            if os.path.getsize(file_name) == 0:
                print("当前没有待办事项")
                return
            
            with open(file_name, 'r', encoding='utf-8') as f:
               content = f.read()
               print('当前待办事项：', content)
               
        except FileExistsError:
            print('读取文件失败')
        
        
def delate_task(file_name):
    char = input('请输入需要删除的任务：')
    
    try:
        with open(file_name, 'r', encoding='utf-8') as f_read:
            with open("task_tamp.txt", 'w', encoding='utf-8') as f_write:
                 for line in f_read:
                    if char in line.strip():
                        new_line = line.replace(char, '')
                        f_write.write(new_line)
    
        os.replace('task_tamp.txt', file_name)
    except FileNotFoundError:
        print('操作失败')
    
    

def get_old_task(file_name):
    old_task = []
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            old_task = f.read()
    except FileNotFoundError:
        print('没有历史任务')

    return old_task     

def main():
    file_name = 'task_list.txt'
    history = get_old_task(file_name)
    
    
    print('历史任务', history)

    while True:
        print("\n====待办事项To-Do Task=====")
        print("1. 查看待办事项")
        print("2. 添加待办事项")
        print("3. 删除待办事项")
        print("4. 退出程序")
        
        choice = input("请选择操作(1-4):")
        
        if choice == '1':
            check_task(file_name)
        elif choice == '2':
            add_task(file_name)
        elif choice == '3':
            delate_task(file_name)
        elif choice == '4':
            print('👋再见')
            return
    
    
if __name__ == '__main__':      
    main()