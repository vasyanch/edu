# Exercise 8(H). Задача: Сортировка массива с помощью кучи с подробным выводом(очередь с приорететом).
#               Метод ООП. Решение через класс.


class Heap(object):

    def __init__(self, massif, n):
        self.dat = massif
        self.n = n
        self.size = n
        
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
        
    def build_heap(self):
        for i in range(self.n - 1, -1, -1):
            self.siftdown(i)
        return self.dat

    def sort(self):
        for i in range(self.size - 1):
            self.dat[self.n - 1], self.dat[0], self.n = self.dat[0], self.dat[self.n - 1], self.n - 1
            self.siftdown(0)
            print(' '.join([str(self.dat[_]) for _ in range(self.n)]))
        return self.dat
            

if __name__ == '__main__':
    size = int(input())
    mas = [int(_) for _ in input().split()]
    heap = Heap(mas, size)
    for _ in heap.build_heap():
        print(_, end=' ')
    print()
    heap.sort()
    print(' '.join([str(heap.dat[_]) for _ in range(heap.size)]))
