class MyEnumerateIterator():
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.index, self.data[self.index]
        self.index += 1
        return value

class MyEnumerate():
    def __init__(self, data):
        self.data = data
    
    def __iter__(self):
        return MyEnumerateIterator(self.data)


enum = MyEnumerate('abcd')

for item in enum:
    print(item)

for item in enum:
    print(item)