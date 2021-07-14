# main

import sys
from read_file import read_file
from lexer import lex
from parser import parse
# from evaluator import evaluate


if __name__ == "__main__":
    rk_file = sys.argv[1]
    for a in parse(lex(read_file(rk_file))):
        print(a)
    # run(sys.argv[1])
