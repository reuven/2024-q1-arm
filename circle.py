class CircleIterator:
    def __init__(self, data, maxtimes):
        self.data = data
        self.maxtimes = maxtimes
        self.index = 0

    def __next__(self):
        if self.index >= self.maxtimes:
            raise StopIteration

        value = self.data[self.index % len(self.data)]
        self.index += 1
        return value

class Circle:
    def __init__(self, data, maxtimes):
        self.data = data
        self.maxtimes = maxtimes

    def __iter__(self):
        return CircleIterator(self.data, self.maxtimes)
