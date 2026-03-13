# 定义语法 - 支持赋值、表达式、print
grammar = r"""
?start: stmt+

stmt: assign | print_stmt

assign: NAME "=" expr

print_stmt: "print" "(" expr ")"

?expr: term
    | expr "+" term   -> add
    | expr "-" term   -> sub

?term: factor
    | term "*" factor -> mul
    | term "/" factor -> div

?factor: NUMBER       -> number
       | NAME         -> var
       | "(" expr ")"

NAME: /[a-zA-Z_][a-zA-Z0-9_]*/
NUMBER: /\d+/

COMMENT: /#[^\n]*/
%import common.WS
%ignore WS
%ignore COMMENT
"""