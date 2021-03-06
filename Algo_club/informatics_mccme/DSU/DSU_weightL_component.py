# Задача №1376. Вес компоненты
# В неориентированный взвешанный граф добавляют ребра. Напишите программу,
# которая в некоторые моменты находит сумму весов ребер в компоненте связности.
# Входные данные
#  В первой строке записано два числа n и m (1≤n,m≤106) - количество вершин в графе и
#  количество производимых добавлений и запросов. Далее следует m строк с описанием добавления или запроса.
#  Каждая строка состоит из двух или четырех чисел. Первое из чисел обозначает код операции.
#  Если первое число 1, то за ним следует еще три числа x, y, w. Это означает, что в граф добавляется ребро из
#  вершины x в вершину y веса w. (1≤x<y≤n, 1≤w≤103). Кратные ребра допустимы.
#  Если первое число 2, то за ним следует ровно одно число x. Это означает,
#  что необходимо ответить на вопрос, какова сумма ребер в компоненте связности, которой принадлежит вершина x (1≤x≤n).
# Выходные данные
#  Для каждой операции с кодом 2 выведите ответ на поставленную задачу.
#  Ответ на каждый запрос выводите на отдельной строке.


class DSU:

    def __init__(self, k):
        self.parent = list(range(n))
        self.rank = [0] * k  # ранк - это глубина дерева
        self.weights = [0] * k  # массив хранящий сумму весов ребер входящиях в данную компоненту связности

#    def make_set(self):
#        self.parent.append(len(self.parent))
#        self.rank.append(0)

    def find_set(self, v):
        if v == self.parent[v]:
            return v
        self.parent[v] = self.find_set(self.parent[v])
        return self.parent[v]

    def union_sets(self, a, b, w):
        a = self.find_set(a)
        b = self.find_set(b)
        if a == b:  # если вершина уже в компоненте то плюсуется только вес добавляемого ребра
            self.weights[a] += w
        else:
            if self.rank[a] < self.rank[b]:
                a, b = b, a
            self.parent[b] = a
            self.weights[a] += w + self.weights[b]
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1


if __name__ == '__main__':
    n, m = map(int, input().split())
    dsu = DSU(n)
    for _ in range(m):
        req = tuple(input().split())
        if req[0] == '1':
            dsu.union_sets(int(req[1]) - 1, int(req[2]) - 1, int(req[3]))
        if req[0] == '2':
            print(dsu.weights[dsu.find_set(int(req[1]) - 1)])
