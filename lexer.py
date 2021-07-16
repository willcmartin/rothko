import re
from stream import stream

class Token():
    def __init__(self, type, val):
        self.type = type
        self.val = val
    def __repr__(self):
        return "type: " + self.type + " value: " + self.val


def lex(char_stream):
    # fill helper function
    def fill(re_values):
        token_val = chars.curr
        while(re.match(re_values, chars.next)):
            token_val += chars.next
            chars.get_next()
        return token_val

    # get character stream
    chars = stream(char_stream)

    # check for each type of token until end of stream
    while chars.next is not None:

        if chars.curr in " \n":
            pass
        elif re.match("[+=-]", chars.curr):
            token_val = fill("[+=-]")
            if token_val in ["+", "-", "=", "=="]:
                yield Token("OPERATOR", token_val)
        elif chars.curr in "();":
            yield Token("SEPERATOR", chars.curr)
        elif re.match("[_a-zA-Z]", chars.curr):
            token_val = fill("[_a-zA-Z]")
            if token_val in ["while", "endwhile", "print"]:
                yield Token("KEYWORD", token_val)
            else:
                yield Token("IDENTIFIER", token_val)
        elif re.match("[0-9]", chars.curr):
            token_val = fill("[0-9]")
            yield Token("INTEGER", token_val)
        else:
            yield Exception(chars.curr + " is not allowed.")

        chars.get_next()
