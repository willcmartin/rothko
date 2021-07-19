# main

import sys
from read_file import read_file
from lexer import lex
from parser import parse
from evaluator import evaluate, Enviornment

def postorder(root):
    #if root is None return
        if root==None:
            return
        #traverse left subtree
        postorder(root.left)
        #traverse right subtree
        postorder(root.right)
        #traverse root
        print(root.data)

if __name__ == "__main__":
    rk_file = sys.argv[1]
    env = Enviornment()
    # evaluate(parse(lex(read_file(rk_file))), env)
    for a in parse(lex(read_file(rk_file))):
        postorder(a)
    # run(sys.argv[1])
