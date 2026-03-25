def main():
    with open('example.txt', 'r', encoding='utf-8') as f:
        #适用于中小型文件
        # count = f.readlines()
        
        # 统计每一行，每有一行就产生一个 1，最后求和
        # count = sum(1 for line in f)
        
        for count, line in enumerate(f, 1):
            pass  # 不做任何操作，只为了让计数器跑完

        print(f"总共有{count}行")
 
 
if __name__ == '__main__':
    main()    
    