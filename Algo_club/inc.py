# фун. inc()  прибавляет 1 к числу в двоичном виде.
# это число храниться в массиве в виде [1, 0, 1, 0, 1]
# разобраться с тем что делает этот алгоритм


def inc(x):    # x - число в виде массива
    n = len(x)
    for i, v in enumerate(x):
        if v == 0:
            break
        if i == n - 1:
            return False
    for j in range(n - 1, i - 1, -1):
        x[j] = abs(x[j] - 1)
    return True
