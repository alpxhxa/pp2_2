#ex 01
class Count:
    def __init__(self, low, high):
        self.current = low
        self.high = high
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        res = self.current
        self.current += 1
        return res

it1 = Count(1, 2)
for x in it1:
    print(x)

#ex 02
class Repeater:
    def __init__(self, val, limit):
        self.val = val
        self.limit = limit
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        self.count += 1
        return self.val

it2 = Repeater("Hi", 2)
for x in it2:
    print(x)

#ex 03
class Double:
    def __init__(self, data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        val = self.data[self.index] * 2
        self.index += 1
        return val

it3 = Double([1, 2])
for x in it3:
    print(x)

#ex 04
class SquareIt:
    def __init__(self, n):
        self.n = n
        self.i = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.i > self.n:
            raise StopIteration
        res = self.i ** 2
        self.i += 1
        return res

it4 = SquareIt(2)
for x in it4:
    print(x)

#ex 05
class Backwards:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

it5 = Backwards([10, 20])
for x in it5:
    print(x)