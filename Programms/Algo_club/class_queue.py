# Структура данных очередь на базе массива.


class Queue:
    def __init__(self, size):
        self.data = [None] * size
        self.start = 0
        self.end = 0
        self.num = 0
        self.size = size

    def push_back(self, a):
        if self.num < self.size:
            self.data[self.end] = a
            self.end = (self.end + 1) % self.size
            self.num += 1
        else:
            return 'full'

    def pop_front(self):
        if self.num > 0:
            ans = self.data[self.start]
            self.start = (self.start + 1) % self.size
            self.num -= 1
            return ans
        else:
            return 'empty'

    def empty(self):
        return self.num
