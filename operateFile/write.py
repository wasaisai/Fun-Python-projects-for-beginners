
def main():
    expr = input('请输入需要写入文件的内容')
    try:
        with open('example.txt', 'a', encoding='utf-8') as f:
            f.write(f"{expr}\n")
        print('已成功写入')
    except FileExistsError:
        print('写入失败')
    
    
if __name__ == '__main__':
    main()