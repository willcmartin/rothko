# main

import sys
from read_file import read_file
from lexer import lex
# from parser import parse
# from evaluator import evaluate




# def run(rk_file):
#
#     # lexer
#     tokens = []
#
#     with open(rk_file, encoding="ascii") as r:
#         for line in r:
#             for char in line:
#                 print(char)
        # char = r.read(1)
        # while(char != ""):
        #     print(char)
        #     print("asdfas")
        #     char = r.read(1)

    # for char in input:
    #     t = lexer(char)
    #     if t is not None:
    #         tokens.append(lexer(char))

    # for t in tokens:
    #     print(t)
    #
    # # parser
    # ast = parse(tokens)
    # print(ast)
    #
    # # evaluator
    # evaluate(ast)


if __name__ == "__main__":
    rk_file = sys.argv[1]
    for a in lex(read_file(rk_file)):
        print(a)
    # run(sys.argv[1])
