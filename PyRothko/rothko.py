"""
PyRothko main
"""

import sys
from read_file import read_file
from lexer import lex
from parser import parse
from evaluator import evaluate
from environment import Environment

if __name__ == "__main__":
    rk_file = sys.argv[1]
    env = Environment()
    evaluate(parse(lex(read_file(rk_file))), env)
