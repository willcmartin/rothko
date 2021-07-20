from stream import stream
from lexer import Token

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



            # def build_ast(node):
            #     tokens.get_next()
            #     if tokens.curr == None or tokens.curr.type in ("SEPERATOR"):
            #         return
            #     else:
            #         if tokens.curr.type in ("INTEGER", "IDENTIFIER"):
            #             node.data = tokens.curr
            #             return build_ast(node)
            #         elif tokens.curr.type in ("OPERATOR"):
            #             if tokens.curr.val in ("+", "-"):
            #                 parent_node = Node()
            #                 parent_node.left = node
            #                 parent_node.data = tokens.curr
            #                 tokens.get_next()
            #                 parent_node.right = build_ast(Node())
            #                 # tokens.get_next()
            #                 # build_ast(parent_node)
            #                 # postorder(parent_node)
            #                 return build_ast(parent_node)
            #             # return parent_node

    # build ast until end of stream

    # while tokens.curr is not None:
    #     curr_node = Node()
    #     while tokens.curr.val != ";":
    #         curr_node = build_ast(curr_node)
    #         tokens.get_next()
    #     yield curr_node
    #     tokens.get_next()


class Node():
    def __init__(self):
        self.right = None # node
        self.data = None # token
        self.left = None # node

class Compound():
    def __init__(self):
        self.data = Token("COMPOUND", "None")
        self.children = []


def parse(token_stream):

    def build_ast(node, left=False):
        if tokens.curr.type in ("SEPERATOR"):
            if tokens.curr.val in (";", ")"):
                return node
            elif tokens.curr.val in ("("):
                tokens.get_next()
                return build_ast(node, left=True)
        else:
            if tokens.curr.type in ("INTEGER", "IDENTIFIER"):
                node.data = tokens.curr
                tokens.get_next()
                if left==True:
                    return build_ast(node)
                else:
                    return node
            elif tokens.curr.type in ("OPERATOR"):
                if tokens.curr.val in ("+", "-", "=="):
                    parent_node = Node()
                    parent_node.left = node
                    parent_node.data = tokens.curr
                    tokens.get_next()
                    parent_node.right = build_ast(Node())
                    return build_ast(parent_node)
                elif tokens.curr.val in ("="):
                    parent_node = Node()
                    parent_node.left = node
                    parent_node.data = tokens.curr
                    tokens.get_next()
                    parent_node.right = build_ast(Node(), left=True)
                    return build_ast(parent_node)
            elif tokens.curr.type in ("KEYWORD"):
                if tokens.curr.val in ("while"):
                    node.data = tokens.curr
                    tokens.get_next()
                    node.left = build_ast(Node(), left=True)
                    node.right = Compound()
                    tokens.get_next()
                    while tokens.curr.val != "endwhile":
                        node.right.children.append(build_ast(Node(), left=True))
                        tokens.get_next()
                    return build_ast(node)
                elif tokens.curr.val in ("endwhile"):
                    tokens.get_next()
                    return build_ast(node, left=True)

    # get token stream
    tokens = stream(token_stream)

    # loop over tokens
    while tokens.curr is not None:
        yield build_ast(Node(), left=True)
        tokens.get_next()
