# main
import sys
from lexer import lexer


def main(rk_file):

    # lexer
    tokens = []

    with open(rk_file) as rk_file_r:
        input = rk_file_r.read()

    for char in input:
        t = lexer(char)
        if t is not None:
            tokens.append(lexer(char))

    for t in tokens:
        t.write()

    # parser





if __name__ == "__main__":
    main(sys.argv[1])
