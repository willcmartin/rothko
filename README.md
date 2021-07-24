# Rothko

A simple programming language with a simple Python interpreter

---

## Run hello world program:

```bash
# clone repo
git clone https://github.com/WillMartin7/rothko.git

# run hello world program through interpreter
python3 PyRothko/rothko.py examples/hello_world.rk
```

## Basic components of Rothko:
- free-form language
- statements end with semicolons
- while loops
    - statements must be inside of a while loop to run
    - every program is initialized with a variable ```main = 1``` (for use in main loop)
    - the simplest terminating program:
    ```python
    while (main == 1)
        main = 0;
    endwhile;
    ```
- conditions are surrounded by parentheses (as seen above in while loop)
- variables
    - all variables are integers
    - variable names must be string of alphabetical characters and underscores
    - declaring a variable:
    ```python
    var = 1;
    ```
- built-in functions
    - read and print
    - called with ```->``` operator
    - example:
    ```python
    read -> var;
    print -> var;
    ```
- conditionals: ```==```, ```>```, ```<```, ```>=```, ```<=```
- operators: ```=```, ```+```, ```-```, ```*```, ```/```

## Example program: ```examples/fibonacci.rk```
```python
while (main == 1)
    read -> terms;
    count = 0;
    n = 0;
    n_next = 1;

    while (count < terms)
        print -> n;

        n_temp = n + n_next;
        n = n_next;
        n_next = n_temp;

        count = count + 1;
    endwhile;

    main = 0;
endwhile;
```

## Interpreter
- written in Python
- hopefully I will write a C version someday
- see [PyRothko](https://github.com/WillMartin7/rothko/tree/main/PyRothko) for details

## TODO:
- order of ops for mathematical statements

## Sources:
- https://accu.org/journals/overload/26/145/balaam_2510/
- https://ruslanspivak.com/lsbasi-part1/

---
---

## General info:

### rothko language
- .rk extension
- language rules
    - all variables [a-z] are integers [0-9]
    - end expressions with ';'

### lexer
- written in python (eventually c)

---

## Notes:

rothko code file -> lexer -> parser -> evaluator

to run: ```python3 rothko.py test.rk```

### rothko language
- free-form (white space doesn't matter)
- interpreted (maybe compiled later)

### lexer
- input: string (source code)
- output: list of tokens
- token
    - things like numbers, strings, operators, punctuation, etc.
    - ID: variable names
    - OPERATOR: +=
    - INT: integer [0-9]
    - SEPERATOR: ;

### parser
- input: list of tokens
- output: abstract syntax tree (ast)
- expression types:
    - assignment (=)
    - operation (+)
    - function (TODO)
- expressions could be held as strings in tuple or as individual classes
- return ast

### evaluator
- fancy stuff

---

## Useful sources

- https://accu.org/journals/overload/26/145/balaam_2510/
- https://www.freecodecamp.org/news/the-programming-language-pipeline-91d3f449c919/
- https://gist.github.com/eliben/5797351
- https://github.com/Rakhyvel/TinyLang
- https://ruslanspivak.com/lsbasi-part9/
- https://www.jayconrod.com/posts/37/a-simple-interpreter-from-scratch-in-python-part-1


## Example code
```
var = 1;

in_loop = 1;
while (in_loop == 1)
    var = var + 1;
    in_loop = 0;
endwhile;

print(var)
```


tokens:
- OPERATOR
    - + = - ==
- SEPERATOR
    - ; ( )
- KEYWORD
    - while, endwhile, print
- IDENTIFIER
    - var ...
- INTEGER
    - 0 1 2 ...

asts:
- assignment
    - ['assignment', 1st ast, 2nd ast]
- comparison
    - ['comparison', condition, 1st ast, 2nd ast]
- arithmetic
    - ['arithmetic', OPERATOR type, 1st ast, 2nd ast]
- loop
    - ['loop', condition, ast]
- print
    - ['print', environment item]
