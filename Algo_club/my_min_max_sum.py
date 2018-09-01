def my_min_first(x):
    # возвр. индекс первого вхождения и значение 
    idn, res = 0, x[0]
    for i, v in enumerate(x):
        if v < res:
            res = v
            idn = i 
    return idn, res

def my_min_last(x):
    # возвр. индекс последнего вхождения и значение 
    idn, res = 0, x[0]
    for i, v in enumerate(x):
        if v <= res:
            res = v
            idn = i 
    return idn, res

def my_min_all(x):
    # возвр. индексы всех вхождений и значение
    indexes = []
    res = x[0]
    for i, v in enumerate(x):
        if v < res:
            indexes.clear()
            res = v
        elif v == res:
            indexes.append(i)
    return indexes, res

def my_max(x):
    res = x[0]
    for i in x:
        if i > res:
            res = i
    return res

def my_sum(x):
    res = 0
    for i in x:
        res += i
    return res
    
def new_m(x):
    y = x[0] * len(x)
    y[0] = x[0]
    for i in range(1, len(x)):
        y.append(x[i] + x[i-1])
    return y


def new_m_(x):
    a = x[0]
    for i in range(1, len(x)):
        x[i] = x[i] + a
        a = x[i] - a
        #print(a)
    return x

def test(n, m):
    from random import randint
    for i in range(n):
        d = [randint(-100, 100) for i in range(m)]
        assert new_m(d) == new_m_(d)
    print('end')


