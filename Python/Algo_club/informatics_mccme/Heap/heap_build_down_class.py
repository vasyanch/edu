# Exercise 7(G). Задача: Построение кучи просеиванием вниз(очередь с приорететом).
#               Метод ООП. Решение через класс.


class Heap(object):

    def __init__(self, massif):
        self.dat = massif
        self.n = len(massif)

    def siftup(self, k):
        while k > 0 and self.dat[k] > self.dat[(k - 1)//2]:
            self.dat[k], self.dat[(k - 1) // 2], k = self.dat[(k - 1) // 2], self.dat[k], (k - 1) // 2
        return k

    def siftdown(self, k):
        while (2 * k + 1) < self.n:
            j = k
            if self.dat[j] < self.dat[2*k + 1]:
                j = 2 * k + 1
            if (2*k + 2) < self.n and self.dat[j] < self.dat[2*k + 2]:
                j = 2 * k + 2
            if k == j:
                break
            else:
                self.dat[k], self.dat[j] = self.dat[j], self.dat[k]
                k = j
        return k
'''
    def extract_max(self):
        if self.n == 0:
            return
        else:
            an = self.dat[0]
            self.dat[0] = self.dat[self.n-1]
            self.n -= 1
            return self.siftdown(0), an
        
    def insert(self, new):  
        if self.n == len(self.dat):
            return
        else:
            self.dat[self.n] = new
            self.n += 1
            return self.siftup(self.n-1)
        
    def del_(self, a):
        if 0 <= a < self.n:  
            an = self.dat[a]
            self.dat[a] = self.dat[self.n-1]
            self.n -= 1
            self.siftup(a)
            self.siftdown(a)
            return an

'''
if __name__ == '__main__':
    n = int(input())
    mas = [int(_) for _ in input().split()]
    heap = Heap(mas)
    for i in range(n // 2, -1, -1):
        heap.siftdown(i)
    for _ in heap.dat:
        print(_, end=' ')
