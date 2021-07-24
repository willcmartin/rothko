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
