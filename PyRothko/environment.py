"""
PyRothko enviornment class

has one scope for the entire program
"""

class Environment():
    def __init__(self):
        self.items = {}
    def set(self, name, val):
        self.items[name] = val
    def get(self, name):
        if name in self.items:
            return self.items[name]
        else:
            return None
    def __repr__(self):
        return str(self.items)
