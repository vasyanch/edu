# Задача №746. Коммерческий калькулятор
# Фирма OISAC выпустила новую версию калькулятора. Этот калькулятор берет с
# пользователя деньги за совершаемые арифметические операции. Стоимость каждой
# операции в долларах равна 5% от числа, которое является результатом операции.
#  На этом калькуляторе требуется вычислить сумму N натуральных чисел (числа известны).
# Нетрудно заметить, что от того, в каком порядке мы будем складывать эти числа,
# иногда зависит, в какую сумму денег нам обойдется вычисление суммы чисел
# (тем самым оказывается нарушен классический принцип “от перестановки мест
# слагаемых сумма не меняется”). Например, пусть нам нужно сложить числа
# 10, 11, 12 и 13. Тогда если мы сначала сложим 10 и 11 (это обойдется нам в 1.05 €),
# потом результат с 12 (1.65 €), и затем с 13 (2.3 €), то всего мы заплатим 5 €,
# если же сначала отдельно сложить 10 и 11 (1.05 €), потом 12 и 13 (1.25 €)
# и, наконец, сложить между собой два полученных числа (2.3 €), то в итоге мы
# заплатим лишь 4.6 €. Напишите программу, которая будет определять, за какую
# минимальную сумму денег можно найти сумму данных N чисел.
# Входные данные:
# Первая строка входных данных содержит число N (2 ≤ N ≤ 105). Во второй строке
# заданы N натуральных чисел, каждое из которых не превосходит 10000.
# Выходные данные:
# Определите, сколько денег нам потребуется на нахождения суммы этих N чисел.
# Результат должен быть выведен с двумя знаками после десятичной точки.

class HeapMin:

    def __init__(self, max_size):
        self.dat = [0] * max_size
        self.n = 0

    def sift_up(self, i):
        while i > 0 and self.dat[(i - 1) // 2] > self.dat[i]:
            self.dat[(i - 1) // 2], self.dat[i], i = \
                self.dat[i], self.dat[(i - 1) // 2], (i - 1) // 2
        return i

    def sift_down(self, i):
        j = i
        while 2 * i + 1 < self.n:
            if self.dat[2 * i + 1] < self.dat[j]:
                j = 2 * i + 1
            if 2 * i + 2 < self.n and self.dat[2 * i + 2] < self.dat[j]:
                j = 2 * i + 2
            if i == j:
                break
            else:
                self.dat[i], self.dat[j] = self.dat[j], self.dat[i]
                i = j
        return i

    def insert(self, new):
        if self.n == len(self.dat):
            return
        else:
            self.dat[self.n] = new
            self.n += 1
            return self.sift_up(self.n - 1)

    def ex_min(self):
        if self.n == 0:
            return
        elif self.n == 1:
            self.n -= 1
            return self.dat[0]
        else:
            ans = self.dat[0]
            self.dat[0] = self.dat[self.n - 1]
            self.n -= 1
            self.sift_down(0)
            return ans

    def build_heap(self, massif):
        self.n = len(massif)
        self.dat = massif
        for _ in range(self.n // 2, -1, -1):
            self.sift_down(_)
        return self.dat


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    heap = HeapMin(0)
    heap.build_heap(lst)
    ch = 0
    while heap.n > 1:
        q = heap.ex_min() + heap.ex_min()
        # print(q)
        ch += q * 0.05
        heap.insert(q)
    print('{:.2f}'.format(ch))
