import shutil

def main():
    #简单拷贝
    shutil.copy('example.txt', 'example01.txt')
    
    # 完整拷贝（保留文件原始日期等信息）
    shutil.copy2('example.txt', 'example02.txt')
    
    with open('example.txt', 'r', encoding='utf-8') as source:
        with open('example03.txt', 'a', encoding='utf-8') as copy_file:
            for line in source:
                # 可对要写入的内容进行处理后，再写入
                copy_file.write(line)

    
if __name__ == '__main__':
    main()