from stream import stream


# TODO: should be function in parse function then don't have to pass tokens
# TODO: remove get_next function?
# def build_ast(prev_ast, get_next=True):
#     if get_next == True:
#         tokens.get_next()
#
#     # base case
#     if tokens.curr.val == ";":
#         return prev_ast
#     # recursive step
#     else:
#         if tokens.curr.type in ("IDENTIFIER", "INTEGER"):
#             return build_ast([tokens.curr.type, tokens.curr.val])
#         elif tokens.curr.type in ("KEYWORD"):
#             if tokens.curr.val in ("while"):
#                 return build_ast(["while", build_ast(None), build_ast(None)], False)
#             if tokens.curr.val in ("endwhile"):
#                 return build_ast(None)
#         elif tokens.curr.type in ("OPERATOR"):
#             if tokens.curr.val in ("="):
#                 next_expression = build_ast(None)
#                 return build_ast(["assignment", "=", prev_ast, next_expression], False)
#             elif tokens.curr.val in ("+"):
#                 next_expression = build_ast(None)
#                 return build_ast(["operation", "+", prev_ast, next_expression], False)
#             elif tokens.curr.val in ("=="):
#                 next_expression = build_ast(None)
#                 return build_ast(["bool", "==", prev_ast, next_expression], False)
#         elif tokens.curr.val in ("()"):
#             if tokens.curr.val == "(":
#                 return build_ast(None)
#             elif tokens.curr.val == ")":
#                 return prev_ast
#

#       loop
# condition    statement


#         loop
#    <             =
# var   1     var2   3


# class Node():
#     def __init__(self, data):
#         self.left = None
#         self.right = None
#         self.data = data


    # construct ast helper function
    # def build_ast(prev_ast, get_next=True):
    #     if get_next == True:
    #         tokens.get_next()
    #
    #     # base case
    #     if tokens.curr.val == ";":
    #         return prev_ast
    #     # recursive step
    #     else:
    #         if tokens.curr.type in ("IDENTIFIER", "INTEGER"):
    #             return build_ast([tokens.curr.type, tokens.curr.val])
    #         elif tokens.curr.type in ("KEYWORD"):
    #             if tokens.curr.val in ("while"):
    #                 return build_ast(["while", build_ast(None), build_ast(None)], False)
    #             if tokens.curr.val in ("endwhile"):
    #                 return build_ast(None)
    #         elif tokens.curr.type in ("OPERATOR"):
    #             if tokens.curr.val in ("="):
    #                 next_expression = build_ast(None)
    #                 return build_ast(["assignment", "=", prev_ast, next_expression], False)
    #             elif tokens.curr.val in ("+"):
    #                 next_expression = build_ast(None)
    #                 return build_ast(["operation", "+", prev_ast, next_expression], False)
    #             elif tokens.curr.val in ("=="):
    #                 next_expression = build_ast(None)
    #                 return build_ast(["bool", "==", prev_ast, next_expression], False)
    #         elif tokens.curr.val in ("()"):
    #             if tokens.curr.val == "(":
    #                 return build_ast(None)
    #             elif tokens.curr.val == ")":
    #                 return prev_ast
    # #
    # class AST():
    #     pass
    #
    # class BinOpNode(AST):
    #     def __init__(self):
    #         self.right = None
    #         self.data = None
    #         self.left = None








        # prev_token = tokens.curr
        #
        # if prev_token.val == seperator_char:
        #     return
        # else:
        #     tokens.get_next()
        #     curr_token = tokens.curr
        #     if curr_token.type in("OPERATOR"):
        #         root.data = curr_token
        #         root.left = Node(prev_token)
        #         root.right = Node(None)
        #         build_ast_2(root.right, ";")
        #     elif curr_token.type in("INTEGER"):
        #         root.data = curr_token
            # elif .type in ("INTEGER"):
            #     root.data =

        # function build_ast():
        # get curr value
        # get next value
        # return Node (left=curr, data=next, build_ast())


class Node():
    def __init__(self):
        self.right = None # node
        self.data = None # token
        self.left = None # node

def parse(token_stream):

    def build_ast(node):
        if tokens.curr.type in ("INTEGER"):
            node.data = tokens.curr
            return node
        elif tokens.curr.type in ("OPERATOR"):
            parent_node = Node()
            parent_node.left = node
            parent_node.data = tokens.curr
            tokens.get_next()
            parent_node.right = build_ast(Node())
            return parent_node

    # get token stream
    tokens = stream(token_stream)

    # build ast until end of stream
    curr_node = Node()
    while tokens.curr.val is not ";":
        curr_node = build_ast(curr_node)
        tokens.get_next()
    yield curr_node
