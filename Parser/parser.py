import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from lark import Lark, Transformer, v_args
from grammar.grammar import grammar

# 创建解析器
parser = Lark(grammar, parser='lalr', debug=False)

def parse_code(code):
    """解析代码，返回 AST"""
    return parser.parse(code)

def run_code(code):
    """解析并执行代码，返回结果"""
    tree = parse_code(code)
    interpreter = Interpreter()
    return interpreter.transform(tree)

class Interpreter(Transformer):
    """解释器：遍历 AST 并执行"""
    
    def __init__(self):
        self.env = {}  # 变量存储
    
    @v_args(inline=True)
    def number(self, token):
        """数字字面量 -> int"""
        return int(token)
    
    @v_args(inline=True)
    def var(self, name):
        """变量引用 -> 查表取值"""
        if name not in self.env:
            raise NameError(f"变量 '{name}' 未定义")
        return self.env[name]
    
    @v_args(inline=True)
    def add(self, left, right):
        return left + right
    
    @v_args(inline=True)
    def sub(self, left, right):
        return left - right
    
    @v_args(inline=True)
    def mul(self, left, right):
        return left * right
    
    @v_args(inline=True)
    def div(self, left, right):
        return left // right  # 整数除法
    
    @v_args(inline=True)
    def assign(self, name, value):
        """赋值语句：存储变量"""
        self.env[name] = value
        return value
    
    @v_args(inline=True)
    def print_stmt(self, value):
        """打印语句"""
        print(value)
        return value
    
    def stmt(self, tree):
        """语句节点：直接返回子节点值"""
        return tree[0]
    
    def start(self, stmts):
        """程序入口：执行所有语句"""
        return stmts[-1] if stmts else None