class Adder:
    def __init__(self, data):
        self.data = data
    def __add__(self, y):
        return self.add(y)
    def add(self, y):
        print('Not Implemented!')

class ListAdder(Adder):
    def add(self, y):
        return self.data + y

class DictAdder(Adder):
    def add(self, y):
        a = {i: y[i] for i in y.keys()}
        for i in (self.data.keys()):
            a[i] = self.data[i] 
        return a

    
