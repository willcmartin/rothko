# parser for Rothko
# expressions: assignment, operation

from stream import stream


# TODO: should be function in parse function then don't have to pass tokens
# TODO: remove get_next function?
def build_ast(tokens, prev_ast, get_next=True):
    if get_next == True:
        tokens.get_next()

    # base case
    if tokens.curr.val == ";":
        return prev_ast
    # recursive step
    else:
        if tokens.curr.type in ("IDENTIFIER", "INTEGER"):
            return build_ast(tokens, [tokens.curr.type, tokens.curr.val])
        elif tokens.curr.type in ("OPERATOR"):
            if tokens.curr.val in ("="):
                next_expression = build_ast(tokens, None)
                return build_ast(tokens, ["assignment", "=", prev_ast, next_expression], False)
            if tokens.curr.val in ("+"):
                next_expression = build_ast(tokens, None)
                return build_ast(tokens, ["operation", "+", prev_ast, next_expression], False)

def parse(token_stream):
    tokens = stream(token_stream)
    while tokens.curr is not None:
        yield build_ast(tokens, None, False)
        tokens.get_next()
