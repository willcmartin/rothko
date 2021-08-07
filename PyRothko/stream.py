"""
PyRothko stream class

convert a generator to a stream with next and curr attributes
"""

class stream():
    def __init__(self, generator):
        self.generator = generator
        self.curr = next(self.generator)
        self.next = next(self.generator)

    def get_next(self):
        self.curr = self.next
        try:
            self.next = next(self.generator)
        except StopIteration:
            self.next = None
