"""
PyRothko parser

returns an abstract syntax tree from program tokens
"""

from stream import stream
from lexer import Token


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
        if tokens.curr.type in ["SEPERATOR"]:
            if tokens.curr.val in (";", ")"):
                return node
            elif tokens.curr.val in ("(", "->"):
                tokens.get_next()
                return build_ast(node, left=True)
        elif tokens.curr.type in ["INTEGER", "IDENTIFIER"]:
            node.data = tokens.curr
            tokens.get_next()
            if left==True:
                return build_ast(node)
            else:
                return node
        elif tokens.curr.type in ["OPERATOR", "CONDITION"]:
            parent_node = Node()
            parent_node.left = node
            parent_node.data = tokens.curr
            if tokens.curr.val in ["="]:
                tokens.get_next()
                parent_node.right = build_ast(Node(), left=True)
                return build_ast(parent_node)
            else:
                tokens.get_next()
                parent_node.right = build_ast(Node())
                return build_ast(parent_node)
        elif tokens.curr.type in ["KEYWORD"]:
            if tokens.curr.val in ["while"]:
                node.data = tokens.curr
                tokens.get_next()
                node.left = build_ast(Node(), left=True)
                node.right = Compound()
                tokens.get_next()
                while tokens.curr.val != "endwhile":
                    node.right.children.append(build_ast(Node(), left=True))
                    tokens.get_next()
                return build_ast(node)
            elif tokens.curr.val in ["print", "printascii", "read"]:
                node.data = tokens.curr
                tokens.get_next()
                node.left = build_ast(Node())
                return build_ast(node)
            elif tokens.curr.val in ["endwhile"]:
                tokens.get_next()
                return build_ast(node, left=True)
        else:
            raise Exception("The token type \"" + tokens.curr.type + "\" is not allowed by the parser.")

    # get token stream
    tokens = stream(token_stream)

    # return ast using token stream
    return build_ast(Node(), left=True)
