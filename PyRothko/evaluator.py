"""
PyRothko evaluator

traverses the ast and carries out the program
while assigning values in the environment
"""

import random
import string

def evaluate(ast, env):

    def evaluate_ast(ast, val=True):
        if ast.data.val == "while":
            while evaluate_ast(ast.left) == True:
                evaluate_ast(ast.right)
        elif ast.data.val == "print":
            print(evaluate_ast(ast.left))
        elif ast.data.val == "printascii":
            print(chr(evaluate_ast(ast.left)))
        elif ast.data.val == "read":
            env.set(evaluate_ast(ast.left, val=False), int(input()))
            print(chr(evaluate_ast(ast.left))) # TODO: is this needed?
        elif ast.data.val == "tape":
            if val == True:
                return env.read_tape(evaluate_ast(ast.left))
            else:
                return 'tapeidx_' + str(evaluate_ast(ast.left))
        elif ast.data.type == "CONDITION":
            if ast.data.val == "==":
                return (evaluate_ast(ast.left) == evaluate_ast(ast.right))
            elif ast.data.val == ">":
                return (evaluate_ast(ast.left) > evaluate_ast(ast.right))
            elif ast.data.val == "<":
                return (evaluate_ast(ast.left) < evaluate_ast(ast.right))
            elif ast.data.val == ">=":
                return (evaluate_ast(ast.left) >= evaluate_ast(ast.right))
            elif ast.data.val == "<=":
                return (evaluate_ast(ast.left) <= evaluate_ast(ast.right))
        elif ast.data.type == "OPERATOR":
            if ast.data.val == "=":
                env.set(evaluate_ast(ast.left, val=False), evaluate_ast(ast.right))
            elif ast.data.val == "+":
                return int(evaluate_ast(ast.left)) + int(evaluate_ast(ast.right))
            elif ast.data.val == "-":
                return int(evaluate_ast(ast.left)) - int(evaluate_ast(ast.right))
            elif ast.data.val == "*":
                return int(evaluate_ast(ast.left)) * int(evaluate_ast(ast.right))
            elif ast.data.val == "/":
                return int(evaluate_ast(ast.left)) // int(evaluate_ast(ast.right))
        elif ast.data.type == "IDENTIFIER":
            if val == True:
                return env.get(ast.data.val)
            else:
                return ast.data.val
        elif ast.data.type == "INTEGER":
            return int(ast.data.val)
        elif ast.data.type == "COMPOUND":
            for child in ast.children:
                evaluate_ast(child)

    def print_ast(ast, lines=set(), level=0, fork=False):
        """print utility for ast"""

        # base case
        if ast.data.val == None:
            return

        # printing
        tree_str = ""
        if level != 0:
            tree_str = ""
            for l in range(level-1):
                if l in lines:
                    tree_str += "│  "
                else:
                    tree_str += "   "
            if fork:
                tree_str += "├── "
                lines.add(level-1)
            else:
                tree_str += "└── "
                lines.discard(level-1)
        print(tree_str + str(ast))

        # recursive cases
        if ast.data.type == "COMPOUND":
            for i, child in enumerate(ast.children):
                if i < (len(ast.children) - 1):
                    print_ast(child, lines, level+1, True)
                else:
                    print_ast(child, lines, level+1, False)
        else:
            if ast.left != None and ast.right != None:
                print_ast(ast.left, lines, level+1, True)
                print_ast(ast.right, lines, level+1, False)
            elif ast.left != None:
                print_ast(ast.left, lines, level+1, False)
            elif ast.right != None:
                print_ast(ast.right, lines, level+1, False)

    # intialize main = 1
    env.set("main", 1)

    # print ast for debugging
    print_ast(ast)

    # call evaluator on ast
    evaluate_ast(ast)

    # print tape for debugging
    # print("tape: ", env)
