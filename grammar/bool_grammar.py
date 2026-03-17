# Boolean + arithmetic grammar (extracted from grammar.py)
# This file is intended to hold the Lark grammar definition for expressions and statements.

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

%import common.WS
%ignore WS
"""
