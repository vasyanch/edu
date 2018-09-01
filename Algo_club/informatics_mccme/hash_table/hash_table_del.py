# Задача №745. Хеширование с удалением.
# Копия задачи 744 с добавлением инструкции:  '- ', означает удаление  строки из множества.


class Hash:
    def __init__(self, n):
        self.table = [0] * 2 * n

    def hash_fun(self, y):
        h = 0
        for v in y:
            h = (ord(v) + h * 42) % 1979
        return h

    def find(self, y):
        val = self.hash_fun(y)
        if self.table[val]:
            if y in self.table[val]:
                return True
        return False

    def add(self, y):
        pos = self.hash_fun(y)
        if self.table[pos]:
            # print(pos)
            if y not in self.table[pos]:
                self.table[pos].append(y)
        else:
            self.table[pos] = []
            self.table[pos].append(y)

    def remove(self, y):
        val = self.hash_fun(y)
        if self.table[val]:
            if y in self.table[val]:
                self.table[self.hash_fun(y)].remove(y)


if __name__ == '__main__':
    h_tab = Hash(10 ** 6)
    while True:
        req = input()
        if req[0:2] == "+ ":
            h_tab.add(req[2:])
        elif req[0:2] == '? ':
            if h_tab.find(req[2:]):
                print('YES')
            else:
                print('NO')
        elif req[0:2] == '- ':
            h_tab.remove(req[2:])
        elif req[0:1] == '#':
            break
