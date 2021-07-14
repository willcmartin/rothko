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


def evaluate_ast(ast, env):
    # env = Enviornment()
    if ast[0] == "assignment":
        env.set(evaluate_ast(ast[2], env), evaluate_ast(ast[3], env))
    elif ast[0] == "operation":
        if ast[1] == "+":
            return evaluate_ast(ast[2], env) + evaluate_ast(ast[3], env)
    elif ast[0] == "INTEGER":
        return int(ast[1])
    elif ast[0] == "IDENTIFIER":
        return ast[1]
    print(env)

def evaluate(ast_stream, env):
    asts = stream(ast_stream)
    while asts.curr is not None:
        print(asts.curr)
        evaluate_ast(asts.curr, env)
        asts.get_next()
