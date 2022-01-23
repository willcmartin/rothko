"""
PyRothko enviornment class

has one scope for the entire program
"""

class Item():
    def __init__(self, name):
        self.name = name
        self.val = None
    def set_val(self, val):
        self.val = val
    def get_val(self):
        return self.val
    def __repr__(self):
        return "(Name: " + self.name + ", Value: " + str(self.val) + ")" # TODO: print next

class Environment():
    def __init__(self):
        self.items = [] # tape

    def set(self, name, val):
        # TODO: this is so hacky, please make better
        if name.startswith('tapeidx_'):
            tape_idx = int(name[8:])

            if tape_idx == len(self.items):
                item = Item(name)
                self.items.append(item)
            elif tape_idx < len(self.items):
                item = self.items[tape_idx]
            else:
                raise Exception("Outside of array range")
        else:
            # TODO: find a better way to see if item exists
            new = True
            for item in self.items:
                if item.name == name:
                    new = False
                    break
            if new:
                item = Item(name)
                self.items.append(item)

        item.set_val(val)
        # item.set_next(next)

    def get(self, name):
        for item in self.items:
            if item.name == name:
                return item.val
        raise Exception("\"" + name + "\" is nowhere to be found in the environment")

    def read_tape(self, pos):
        if pos < len(self.items):
            return self.items[pos].val
        else:
            raise Exception("your tape isn't that long")

    def __repr__(self):
        return str(self.items)

# intialized with empty tape
# every variable created is sequentially added to tape
# del var_name; removes variable from tape no matter location, shifts other variables
# elements accessed or set with tape[idx]; if set, no name to reference variable (given random string name)
# representation in ast? "tape -> idx" same as "var_name"
