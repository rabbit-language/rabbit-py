# 定义语法 - 支持赋值、表达式、print
grammar = r"""
?start: stmt+

stmt: var_decl 
    | assign 
    | print_stmt

var_decl: NAME ":" type ("=" expr)?

type: "Int" | "Float" | "String" | "Bool"

assign: NAME "=" expr

print_stmt: "print" "(" expr ")"

// 表达式层级（从高到低优先级）
?expr: compare

?compare: add
    | compare ">" add   -> gt
    | compare "<" add   -> lt
    | compare ">=" add  -> ge
    | compare "<=" add  -> le
    | compare "==" add  -> eq

?add: term
    | add "+" term   -> add
    | add "-" term   -> sub

?term: factor
    | term "*" factor -> mul
    | term "/" factor -> div

?factor: NUMBER       -> number
       | NAME         -> var
       | BOOL         -> bool
       | "(" expr ")"

// 新增：布尔值关键字
BOOL: "true" | "false"

NAME: /[a-zA-Z_][a-zA-Z_0-9]*/
NUMBER: /\d+(\.\d+)?/

COMMENT: /#[^\n]*/
%import common.WS
%ignore WS
%ignore COMMENT
"""