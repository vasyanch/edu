# Exercise 5(E). Задача: Приорететная очередь  с удалением(очередь с приорететом).
#               Метод ООП. Решение через класс.


class Heap(object):

    def __init__(self, max_size):
        self.dat = [0] * max_size
        self.n = 0

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
        if self.n:
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


if __name__ == '__main__':
    N, M = tuple(map(int, input().split()))
    queue = Heap(N)
    for _ in range(M):
        req = tuple(map(int, input().split()))
        if req[0] == 1:
            ans = queue.extract_max()
            if ans is None:
                print(-1)
            elif ans[0] == 0 and queue.n == 0:
                print(ans[0], ans[1])
            else:
                print(ans[0] + 1, ans[1])
        elif req[0] == 2:
            ans = queue.insert(req[1])
            if ans is None:
                print(-1)
            else:
                print(ans + 1)
        elif req[0] == 3:
            ans = queue.del_(req[1] - 1)
            if ans is None:
                print(-1)
            else:
                print(ans)
    for i in range(queue.n):
        print(queue.dat[i], end=' ')
