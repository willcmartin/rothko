# parser for Rothko
# expressions: assignment, operation

# some examples:
#
# a = 1;
# (assignment, a, 1)
#
# 1 + 2;
# (operation, +, 1, 2)
#
# a = 1 + 2;
# (assignment, a, (operation, +, 1, 2))

# class TokenStream():
#     def __init__(self, tokens):
#         self.tokens = tokens

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.idx = -1

    @property
    def curr_token(self):
        return self.tokens[self.idx]

    @property
    def next_token(self):
        try:
            return self.tokens[self.idx+1]
        except IndexError:
            return None

    @property
    def prev_token(self):
        try:
            return self.tokens[self.idx-1]
        except IndexError:
            return None

    # recursive function
    def build_ast(self, prev_expression):
        self.idx += 1
        print(self.idx)
        # base case
        if self.curr_token.type == "SEPERATOR":
            self.idx -= 1
            return prev_expression

        # recursive step
        else:
            if self.curr_token.type in ("ID", "INT"):
                return self.build_ast(self.curr_token)
            elif self.curr_token.type == "OPERATOR":
                if self.curr_token.val == "=":
                    next_expression = self.build_ast(None)
                    return self.build_ast(("assignment", "=", prev_expression, next_expression))
                elif self.curr_token.val == "+":
                    next_expression = self.build_ast(None)
                    return self.build_ast(("operation", "+", prev_expression, next_expression))

def parse(tokens):
    parser = Parser(tokens)
    return parser.build_ast(None)
