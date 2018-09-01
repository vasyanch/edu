# Задача №744. Хеширование
# Реализуйте структуру данных типа “множество строк”. Хранимые строки  – непустые последовательности
# длиной не более 10 символов, состоящие из строчных латинских букв. Структура данных должна поддерживать
# операции добавления строки в множество и проверки принадлежности  данной строки множеству.
# Максимальное количество элементов в хранимом множестве не превосходит 106.
# Входные данные:
#   Каждая строка входных данных задает одну операцию над множеством. Запись операции состоит из типа
#   операции и следующей за ним через пробел строки, над которой проводится операция. Тип операции  –
#   один из двух символов: +  означает добавление данной строки в множество;
#   ?  означает проверку принадлежности данной строки множеству.
#   Общее количество операций во входном файле не превосходит 10^6. Список операций завершается строкой, в которой
#   записан один символ # – признак конца входных данных. При добавлении элемента в множество НЕ ГАРАНТИРУЕТСЯ,
#   что он отсутствует в этом множестве.
# Выходные данные:
#   Программа должна вывести для каждой операции типа ? одну из двух строк YES или NO, в зависимости от того,
#   встречается ли данное слово в нашем множестве.


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


if __name__ == '__main__':
    h_tab = Hash(5 * 10 ** 3)
    while True:
        req = input()
        if req[0:2] == "+ ":
            h_tab.add(req[2:])
        elif req[0:2] == '? ':
            if h_tab.find(req[2:]):
                print('YES')
            else:
                print('NO')
        elif req[0:1] == '#':
            break
    '''
    from random import choice
    from string import ascii_letters 
    for _ in range(10 ** 2):
        h_tab.add(''.join(choice(ascii_letters) for _ in range(10)))
    print(len(h_tab.table))
    for i in range(0, len(h_tab.table), 10):
        print(h_tab.table[i], end='\n\n')
    '''