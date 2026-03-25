def add_task(task_list):
    expr = input('请输入需要添加的待办事项, 若多项请用空格隔开')
    input_list = expr.split()
    return task_list + input_list

def check_task(task_list):
    
    if len(task_list) == 0:
        print('当前没有任何待办事项')
        return
    else:
        print('当前待办事项：')
        for i in range(len(task_list)):
            print(i + 1, ':', task_list[i])
        
def delate_task(task_list):
    char = input('请输入需要删除的任务：')
    
    if char in task_list:
        task_list.remove(char)
    else:
        input('当前任务列表没有此项任务')
        

def main():

    task_list = []
    while True:
        print("\n====待办事项To-Do Task=====")
        print("1. 查看待办事项")
        print("2. 添加待办事项")
        print("3. 删除待办事项")
        print("4. 退出程序")
        
        choice = input("请选择操作(1-4):")
        
        if choice == '1':
            check_task(task_list)
        elif choice == '2':
            task_list = add_task(task_list)
            print(f"当前列表已更新: {task_list}")
        elif choice == '3':
            delate_task(task_list)
            print(f"当前列表已更新: {task_list}")
        elif choice == '4':
            print('👋再见')
            return
    
    
if __name__ == '__main__':      
    main()