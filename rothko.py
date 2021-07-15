# main

import sys
from read_file import read_file
from lexer import lex
from parser import parse
from evaluator import evaluate, Enviornment


if __name__ == "__main__":
    rk_file = sys.argv[1]
    env = Enviornment()
    # evaluate(parse(lex(read_file(rk_file))), env)
    for a in lex(read_file(rk_file)):
        print(a)
    # run(sys.argv[1])
