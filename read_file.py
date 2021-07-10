# generator for character stream

def read_file(rk_file):
    with open(rk_file, encoding="ascii") as r:
        for line in r:
            for char in line:
                yield(char)
