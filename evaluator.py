# evaluator for rothko

from stream import stream

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
    # def postorder(root):
    #     #if root is None return
    #     if root==None:
    #         return
    #     #traverse left subtree
    #     try:
    #         postorder(root.left)
    #     except AttributeError:
    #         pass
    #     #traverse right subtree
    #     try:
    #         postorder(root.right)
    #     except AttributeError:
    #         for child in root.children:
    #             postorder(child)
    #     #traverse root
    #     evaluate_ast(root.data)
    #

    def evaluate_ast(ast, val=True):
        if ast.data.val == "while":
            while evaluate_ast(ast.left) == True:
                evaluate_ast(ast.right)
                # print(env.items["main"])
                # print(env.items["var"])
        elif ast.data.val == "print":
            print(evaluate_ast(ast.left))
        elif ast.data.val == "printascii":
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
                # print(evaluate_ast(ast.left))
                # print(evaluate_ast(ast.right))
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

    env.set("main", 1)
    evaluate_ast(ast)

        # if ast[0] == "assignment":
        #     env.set(evaluate_ast(ast[2], env), evaluate_ast(ast[3], env))
        # elif ast[0] == "operation":
        #     if ast[1] == "+":
        #         return evaluate_ast(ast[2], env) + evaluate_ast(ast[3], env)
        # elif ast[0] == "INTEGER":
        #     return int(ast[1])
        # elif ast[0] == "IDENTIFIER":
        #     if ast[1] in env.items:
        #         return env.items[ast[1]]
        #     else:
        #         return ast[1]


    # asts = stream(ast_stream)
    # tokens_stream = postorder(ast)
    # tokens = stream(tokens_stream)
    # while tokens.curr is not None:
    #     evaluate_ast(tokens)
    #     tokens.get_next()
