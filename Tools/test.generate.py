# test_generator.py
import os

def create_test_file(target_file, func_name):
    test_file = f"test_{target_file}"
    if os.path.exists(test_file):
        print(f"⚠️ {test_file} 已存在，跳过生成。")
        return

    content = f"""import unittest
from {target_file.replace('.py', '')} import {func_name}

class Test{func_name.capitalize()}(unittest.TestCase):
    def test_basic_sort(self):
        self.assertEqual({func_name}(), )
        
    def test_empty(self):
        self.assertEqual({func_name}([]), [])

    def test_reverse(self):
        self.assertEqual({func_name}(), )

if __name__ == '__main__':
    unittest.main()
"""
    with open(test_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ 已为您自动创建测试脚本: {test_file}")

if __name__ == "__main__":
    # 这里可以根据需要修改文件名和函数名
    create_test_file("my_sort.py", "bubble_sort")
