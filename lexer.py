# lexer for Rothko

import re
from stream import stream

class Token():
    def __init__(self, type, val):
        self.type = type
        self.val = val
    def __repr__(self):
        return "type: " + self.type + " value: " + self.val


def lex(char_stream):
    chars = stream(char_stream)
    while chars.next is not None:
        if chars.curr in " \n":
            pass
        elif chars.curr in "+-=":
            yield Token("OPERATOR", chars.curr)
        elif chars.curr in ";":
            yield Token("SEPERATOR", chars.curr)
        elif re.match("[_a-zA-Z]", chars.curr):
            yield Token("ID", chars.curr)
        elif re.match("[.0-9]", chars.curr):
            yield Token("INT", chars.curr)
        else:
            yield Exception(chars.curr + " is not allowed. Be less dumb.")
        chars.get_next()
