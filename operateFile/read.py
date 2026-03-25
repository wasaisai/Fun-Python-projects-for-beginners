def main():
    name = input('请输入需要读取的文件名')
    try:
        with open(f"{name}.txt", 'r', encoding='utf-8') as f:
            content = f.read()
            print("--- 文件内容如下 ---")
            print(content)
    except FileNotFoundError:
           print(f'读取失败：当前目录下找不到名为 "{name}.txt" 的文件')
        
if __name__ == '__main__':
    main()