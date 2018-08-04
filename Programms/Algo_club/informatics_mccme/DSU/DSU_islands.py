# Задача №1375. Острова.
# Одно разбросанное на островах Океании государство решило создать сеть автомобильных дорог (вернее, мостов).
# По каждому мосту можно перемещаться в обе стороны. Был разработан план очередности строительства мостов и известно,
# что после постройки всех мостов можно будет проехать по ним с каждого острова на каждый
# (возможно, через некоторые промежуточные острова).
# Однако, этот момент может наступить до того, как будут построены все мосты. \
# Вам необходимо определить такое минимальное количество мостов, после строительства которых
# (в порядке, определенном планом), можно будет попасть с любого острова на любой другой.

# Входные данные
# Первая строка содержит два числа: число островов N (1≤N≤10000) и количество мостов в плане M (1≤M≤50000).
# Далее идет M строк, каждая содержит два числа x и y (1≤x,y≤N) - номера городов,
# которые соединяет очередной мост в плане.
# Выходные данные
# Программа должна вывести единственное число - минимальное количество построенных мостов,
# после которого можно будет попасть с любого острова на любой другой.


class DSU:

    def __init__(self, k):
        self.parent = list(range(k))
        self.rank = [1] * k  # ранк - это размер множества(кол-во элементов в нем)

    def make_set(self):
        self.parent.append(len(self.parent))
        self.rank.append(1)

    def find_set(self, v):
        if v == self.parent[v]:
            return v
        self.parent[v] = self.find_set(self.parent[v])
        return self.parent[v]

    def union_sets(self, a, b):
        a = self.find_set(a)
        b = self.find_set(b)
        if a != b:
            if self.rank[a] < self.rank[b]:
                a, b = b, a
            self.parent[b] = a
            self.rank[a] += self.rank[b]

if __name__ == '__main__':
    n, m = map(int, input().split())
    dsu = DSU(n)
    ch = 0
    for i in range(m):
        x, y = map(int, input().split())
        dsu.union_sets(x - 1, y - 1)
        ch += 1
        if dsu.rank[dsu.find_set(x - 1)] >= n or dsu.rank[dsu.find_set(y - 1)] >= n:
            print(ch)
            break