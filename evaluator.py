# enviornment with one scope for the entire program
class Enviornment():
    def __init__(self):
        self.items = {}
    def set(self, name, val):
        self.items[name] = val
    def get(self, name):
        if name in self.items:
            return self.items[name]
        else:
            return None
    def __repr__(self):
        return str(self.items)


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
            print(chr(evaluate_ast(ast.left)))
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
            if val==True:
                return env.items[ast.data.val]
            else:
                return ast.data.val

        elif ast.data.type == "INTEGER":
            return int(ast.data.val)
        elif ast.data.type == "COMPOUND":
            for child in ast.children:
                evaluate_ast(child)

    # intialize main = 1
    env.set("main", 1)

    # call evalusator on ast
    evaluate_ast(ast)
