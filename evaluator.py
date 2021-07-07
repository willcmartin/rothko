# evaluator for rothko

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


def evaluate(ast):
    env = Enviornment()
    if ast[0] == "assignment":
        env.set(evaluate(ast[2]), evaluate(ast[3]))
    elif ast[0] == "operation":
        if ast[1] == "+":
            return evaluate(ast[2]) + evaluate(ast[3])
    elif ast[0] == "INT":
        return int(ast[1])
    elif ast[0] == "ID":
        return ast[1]
    print(env)
