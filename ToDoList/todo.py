FILENAME = "text.txt"
def load_tasks():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return[]
    
def save_tasks(tasks):
    with open(FILENAME, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task +"\n")

tasks = load_tasks()

while True:
    print("\n====待办事项To-Do list=====")
    print("1. 查看待办事项")
    print("2. 添加待办事项")
    print("3. 删除待办事项")
    print("4. 退出程序")
    
    choice = input("请选择操作(1-4):")
    
    if choice == "1":
        print("\n当前待办事项:")
        if not tasks:
            print("(暂无待办事项)")
        else:
            for i, task in enumerate(tasks, start = 1):
                #🧠 enumerate 到底是干嘛的？它用来：在遍历列表时，同时拿到“索引 + 元素”
                #start是索引，task 是tasks里面的元素
                print(f"{i}.{task}")
                #👉 这是 Python 的 f-string（格式化字符串），把变量的值，直接塞进字符串里
                #👉 f"..." 是“能在字符串里直接用变量”的写法
                #👉 Python 3.6+ 强烈推荐用它
                #👉 {} 里放变量或表达式
    
    elif choice =="2":
        task = input("请输入待办事项:")
        tasks.append(task)
        save_tasks(tasks)
        print("✅添加成功！")
        
    elif choice =="3":
        if not tasks:
            print("没有可删除的事项")
        else:
            for i, task in enumerate(tasks, start=1):
                # print(f"{i}.{task}")
                num = input("请输入要删除的编号:")
                
                #👉 isdigit() = “这串字符能不能当数字用？”
                if num.isdigit():
                    num = int(num)
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        save_tasks(tasks)
                        print(f"🗑️已删除: {removed}")
                    else:
                        print("编号超出范围")
                else:
                    print("请输入数字")
        
    elif choice == "4":
        print("再见 👋")
        break
    
    else:
        print("❌无效输入，请重新选择")
    