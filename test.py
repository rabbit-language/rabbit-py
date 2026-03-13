from Parser.parser import run_code

# 从文件读取测试代码
with open('test/test.ribt', 'r', encoding='utf-8') as f:
    test_code = f.read()

if __name__ == "__main__": 
    result = run_code(test_code)