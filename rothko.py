# main
import sys
from lexer import lexer
from parser import parse


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
        print(t)

    # parser
    ast = parse(tokens)
    print(ast)

    # evaluator


if __name__ == "__main__":
    main(sys.argv[1])
