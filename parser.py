# parser for Rothko
# expressions: assignment, operation

from stream import stream

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

# class Parser:
#     def __init__(self, tokens):
#         self.tokens = tokens
#         self.idx = -1
#
#     @property
#     def curr_token(self):
#         return self.tokens[self.idx]
#
#     @property
#     def next_token(self):
#         try:
#             return self.tokens[self.idx+1]
#         except IndexError:
#             return None
#
#     @property
#     def prev_token(self):
#         try:
#             return self.tokens[self.idx-1]
#         except IndexError:
#             return None

# recursive function
# def build_ast(self, prev_expression):
#     self.idx += 1
#     # base case
#     if self.curr_token.type == "SEPERATOR":
#         self.idx -= 1
#         return prev_expression
#
#     # recursive step
#     else:
#         if self.curr_token.type in ("ID", "INT"):
#             return self.build_ast((self.curr_token.type, self.curr_token.val))
#         elif self.curr_token.type == "OPERATOR":
#             if self.curr_token.val == "=":
#                 next_expression = self.build_ast(None)
#                 return self.build_ast(("assignment", "=", prev_expression, next_expression))
#             elif self.curr_token.val == "+":
#                 next_expression = self.build_ast(None)
#                 return self.build_ast(("operation", "+", prev_expression, next_expression))

# should be function in parse function then don't have to pass tokens
def build_ast_new(tokens, prev_ast, get_next=True):
    if get_next == True:
        tokens.get_next()

    # base case
    if tokens.curr.val == ";":
        return prev_ast
    # recursive step
    else:
        if tokens.curr.type in ("IDENTIFIER", "INTEGER"):
            return build_ast_new(tokens, tokens.curr)
        elif tokens.curr.type in ("OPERATOR"):
            if tokens.curr.val in ("="):
                next_expression = build_ast_new(tokens, None)
                return build_ast_new(tokens, ["assignment", "=", prev_ast, next_expression], False)
            if tokens.curr.val in ("+"):
                next_expression = build_ast_new(tokens, None)
                return build_ast_new(tokens, ["operation", "+", prev_ast, next_expression], False)




def parse(token_stream):
    tokens = stream(token_stream)
    while tokens.curr is not None:
        yield build_ast_new(tokens, None, False)
        tokens.get_next()
    # parser = Parser(tokens)
    # return parser.build_ast(None)
