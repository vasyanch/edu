class Set:
    def __init__(self, value = []):
        self.data = []
        self.concat(value)

    def intersect(self, other):
        res = []
        for x in other:
            if x in self.data:
                res.append(x)
        return Set(res)

    def union(self, other):
        res = self.data[:]
        for x in other:
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:
            if not x in self.data:
                self.data.append(x)

    def __add__(self, other):
        return Set(list.__add__(self.data, other))

    def __len__(self):
       return len(self.data) 

    def __getitem__(self, key): return self.data[key] # self[i]

    def __and__(self, other): return self.intersect(other) # self & other

    def __or__(self, other): return self.union(other) # self | other

    def __repr__(self): return 'Set:' + repr(self.data) # Вывод

class MultiSet(Set):
    
    def intersect(self, *args):
        res = []
        for arg in args:
            for x in arg:
                if x in self.data:
                    res.append(x)
        return Set(res)

    def union(self, *args):
        res = self.data[:]
        for arg in args:
            for x in arg:
                if not x in res:
                    res.append(x)
        return Set(res)            
