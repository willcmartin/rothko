# parser for Rothko
# expressions: assignment, operation

from stream import stream


# TODO: should be function in parse function then don't have to pass tokens
# TODO: remove get_next function?
def build_ast(prev_ast, get_next=True):
    if get_next == True:
        tokens.get_next()

    # base case
    if tokens.curr.val == ";":
        return prev_ast
    # recursive step
    else:
        if tokens.curr.type in ("IDENTIFIER", "INTEGER"):
            return build_ast([tokens.curr.type, tokens.curr.val])
        elif tokens.curr.type in ("KEYWORD"):
            if tokens.curr.val in ("while"):
                return build_ast(["while", build_ast(None), build_ast(None)], False)
            if tokens.curr.val in ("endwhile"):
                return build_ast(None)
        elif tokens.curr.type in ("OPERATOR"):
            if tokens.curr.val in ("="):
                next_expression = build_ast(None)
                return build_ast(["assignment", "=", prev_ast, next_expression], False)
            elif tokens.curr.val in ("+"):
                next_expression = build_ast(None)
                return build_ast(["operation", "+", prev_ast, next_expression], False)
            elif tokens.curr.val in ("=="):
                next_expression = build_ast(None)
                return build_ast(["bool", "==", prev_ast, next_expression], False)
        elif tokens.curr.val in ("()"):
            if tokens.curr.val == "(":
                return build_ast(None)
            elif tokens.curr.val == ")":
                return prev_ast


def parse(token_stream):
    global tokens
    tokens = stream(token_stream)
    while tokens.curr is not None:
        yield build_ast(None, False)
        tokens.get_next()
