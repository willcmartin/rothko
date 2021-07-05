# lexer for Rothko
# python3 lexer.py test.rk

import sys
import re

class Token():
    def __init__(self, type, val):
        self.type = type
        self.val = val
    def __repr__(self):
    # def write(self):
        return "type: " + self.type + " value: " + self.val

def lexer(c):
    if c in " \n":
        return None
    elif c in "+-=":
        return Token("OPERATOR", c)
    elif c in ";":
        return Token("SEPERATOR", c)
    elif re.match("[_a-zA-Z]", c):
        return Token("ID", c)
    elif re.match("[.0-9]", c):
        return Token("INT", c)
    else:
        raise Exception(c + " is not allowed. Be less dumb.")


# if __name__ == '__main__':
#     tokens = []
#
#     with open(sys.argv[1]) as rk_file:
#         input = rk_file.read()
#
#     for char in input:
#         t = lexer(char)
#         if t is not None:
#             tokens.append(lexer(char))
#
#     for t in tokens:
#         t.write()
