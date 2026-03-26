import json
import datetime
def load_config():
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
        
    return config

def my_loger(message, level="INFO"):
    config = load_config()['log_config']
    log_type = config[level]
    time_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_name = log_type['file'] + '_' + time_str
    
    with open(file_name, 'a', encoding='utf-8') as f:
       f.write("开始记录日志...\n")
       f.write(message)

def main():
   my_loger('启动日志', 'INFO')
        
        
if __name__ == '__main__':
    main()