"""
PyRothko enviornment class

has one scope for the entire program
"""

class Item():
    def __init__(self, name):
        self.name = name
        self.val = None
        self.next = None
    def set_val(self, val):
        self.val = val
    def get_val(self):
        return self.val
    def set_next(self, next):
        self.next = next
    def get_next(self):
        return self.next
    def __repr__(self):
        return "(Name: " + self.name + ", Value: " + str(self.val) + ")" # TODO: print next

class Environment():
    def __init__(self):
        self.items = []

    def add(self, name, val, next=None):
        # TODO: find a better way to see if item exists
        new = True
        for item in self.items:
            if item.name == name:
                new = False
                break
        if new:
            item = Item(name)

        item.set_val(val)
        item.set_next(next)

        if new:
            self.items.append(item)

    def get(self, name):
        for item in self.items:
            if item.name == name:
                return item.val
        raise Exception("\"" + name + "\" is nowhere to be found in the environment")

    def __repr__(self):
        return str(self.items)
