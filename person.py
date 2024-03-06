
class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __repr__(self):
        return f'{self.first} {self.last}'
