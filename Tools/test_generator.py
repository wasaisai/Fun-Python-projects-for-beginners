import os
import re
import shutil

def find_all_testable_functions(file_path):
    """扫描文件，找出所有处于激活状态（未被注释）的函数名"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 匹配行首的 def，忽略被 # 注释掉的行
    active_funcs = re.findall(r'^\s*def\s+(\w+)\s*\(', content, re.MULTILINE)
    
    # 排除掉不需要测试的逻辑
    exclude_list = ['main', 'get_input_str', 'get_input', 'input_data']
    testable_funcs = [f for f in active_funcs if f not in exclude_list]
    return testable_funcs

def create_tests():
    test_dir = "tests"
    
    # --- 💡 新增：清理逻辑 ---
    if os.path.exists(test_dir):
        print(f"🧹 正在清理旧的测试脚本...")
        for item in os.listdir(test_dir):
            # 仅删除以 test_ 开头的 .py 文件，保留 __init__.py 和其他自定义文件
            if item.startswith("test_") and item.endswith(".py"):
                os.remove(os.path.join(test_dir, item))
    else:
        os.makedirs(test_dir)
    
    # 确保 __init__.py 始终存在
    with open(os.path.join(test_dir, "__init__.py"), "w") as f: pass

    # --- 💡 生成逻辑 ---
    files = [f for f in os.listdir('.') if f.endswith('.py') and not f.startswith('test')]
    
    for py_file in files:
        module_name = py_file.replace('.py', '')
        functions = find_all_testable_functions(py_file)
        
        if not functions:
            continue

        test_file_path = os.path.join(test_dir, f"test_{module_name}.py")
        import_stmt = f"from {module_name} import {', '.join(functions)}"
        
        test_methods = ""
        for func in functions:
            test_methods += f"""
    def test_{func}(self):
        print(f"\\n🧪 正在测试函数: {func}")
        # data = 
        # self.assertEqual({func}(data), "预期结果")
"""

        content = f"""import unittest
import sys
import os

# 将上一级目录加入系统路径
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

{import_stmt}

class Test{module_name.replace('_', '').capitalize()}(unittest.TestCase):
{test_methods}
if __name__ == '__main__':
    unittest.main()
"""
        with open(test_file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ 已同步生成: {test_file_path} (函数: {', '.join(functions)})")

if __name__ == "__main__":
    create_tests()
    print("\\n✨ 所有测试脚本已刷新！")
