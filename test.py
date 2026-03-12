from Parser.parser import Interpreter, parse_code, run_code  # 导入函数，不要导入 tree

test_code = """
# Rabbit 语言测试
a = 10
b = 20
print(a + b)
"""

if __name__ == "__main__":
    # 方法A：分步执行
    tree = parse_code(test_code)  # 先解析得到 tree
    interpreter = Interpreter()
    result = interpreter.transform(tree)  # 再执行
    print(f"执行结果: {result}")
    
    # 或者方法B：一步到位
    # result = run_code(test_code)