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

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.idx = 0

    @property
    def curr_token(self):
        return self.tokens[self.idx]

    @property
    def next_token(self):
        try:
            return self.tokens[self.idx+1]
        except IndexError:
            return None

    # recursive function
    def build_ast(self, prev_expression):
        # base case
        if (self.next_token == None):
            return prev_expression

        # recursive step
        else:
            print(self.curr_token.val)
            self.idx += 1
            return self.build_ast((prev_expression,"asd"))






        # print(prev)
        # if self.iterator <= len(self.tokens):
        #     if self.tokens[self.iterator].type == "SEPERATOR":
        #         return prev
        #     elif self.tokens[self.iterator].type == "ID" and self.tokens[self.iterator+1].type == "OPERATOR":
        #         if self.tokens[self.iterator+1].val == "+":
        #             self.iterator += 3
        #             return self.next_expression(("operation", "+", self.tokens[self.iterator].val, self.tokens[self.iterator+2].val))
        #         elif self.tokens[self.iterator+1].val == "=":
        #             self.iterator += 2
        #             return self.next_expression(("assignment", self.tokens[self.iterator].val, self.tokens[self.iterator+1].val))
        #

def parse(tokens):
    parser = Parser(tokens)
    return parser.build_ast(None)
