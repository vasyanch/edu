class MyList():
    def __repr__(self):
        return 'MyList: {0}'.format(self.data)
    
    def __init__(self, start=[]):
        self.data = []
        for i in start: self.data.append(i)

    def __radd__(self, other):
        a = self.__class__
        print('Calls: {0}\nSum {1}: {2} and {3}:'.format(n,
            self.__class__.__name__, self.data, other))
        if not isinstance(other, MyList):
            return a((list.__add__(other, self.data)))
        if isinstance(other, MyList) or isinstance(other, MyListSub):
            return a((list.__add__(other.data, self.data)))           

    def __add__(self, other):
        a = self.__class__
        print('Sum {0}: {1} and {2}:'.format(
            self.__class__.__name__, self.data, other))
        if not isinstance(other, MyList):
            return a((list.__add__(self.data, other)))
        if isinstance(other, MyList) or isinstance(other, MyListSub):
            return a((list.__add__(self.data, other.data)))
    
    def __getitem__(self, index):
        print('{0} at index {1}'.format(
            list.__getitem__(self.data, index), index))
        return list.__getitem__(self.data, index)

    def __iter__(self):
        print('Iterator')
        return list.__iter__(self.data)

    def append(self, item):
        print('Add {0} to end of {1}'.format(item, self))
        return self.data.append(item)

    def sort(self):
        print('Sorted')
        return self.data.sort()
    

class MyListSub(MyList):
    calls = 0

    def __init__(self, start=[]):
        self.add = 0
        MyList.__init__(self, start)

    def __add__(self, other):
        MyListSub.calls +=1
        self.add += 1
        return MyList.__add__(self, other)

    def stat(self):
        print(self.calls, self.add)
        

           
    def __repr__(self):
        return 'MyListSub: {0}'.format(self.data)
