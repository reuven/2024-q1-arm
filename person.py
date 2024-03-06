
class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __repr__(self):
        return f'{self.first} {self.last}'

    def initials(self):
        return f'{self.first[0]} {self.last[0]}'

    def initials_are(self, other):
        return f'{self.first[0]} {self.last[0]}' == other
