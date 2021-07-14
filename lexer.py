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
        elif chars.curr in "();":
            yield Token("SEPERATOR", chars.curr)
        elif re.match("[_a-zA-Z]", chars.curr):
            id = chars.curr
            while (re.match("[_a-zA-Z0-9]", chars.next)):
                id += chars.next
                chars.get_next()
            if id in ["if", "endif", "loop", "endloop", "exitloop", "print"]:
                yield Token("KEYWORD", id)
            else:
                yield Token("IDENTIFIER", id)
        elif re.match("[0-9]", chars.curr):
            int = chars.curr
            while (re.match("[0-9]", chars.next)):
                int += chars.next
                chars.get_next()
            yield Token("INTEGER", int)
        else:
            yield Exception(chars.curr + " is not allowed. Be less dumb.")
        chars.get_next()
