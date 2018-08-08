# Задача 378 с сайта LeetCode
# Поиск k - ой порядковой статистики в матрице отсортированой по строкам и
# столбцам.


def count_less(matrix, v, n):
    '''
    Данная функция возвращает кол-во элементов матрицы строго меньших заданного
    значения v, n - размер матрицы.
    '''
    p, q = 0, n - 1  # p - number of row, q - number of colum
    s = 0
    while p < n and q > -1:
        while q > -1 and matrix[p][q] >= v:
            q -= 1
        s += (q + 1)
        p += 1
    return s


def search(m, k):
    '''
Двоичный поиск. Постепеное приближение к   k - ой статистике. 
    '''
    n = len(m)
    a, b = m[0][0], m[n - 1][n - 1] + 1
    while (b - a) > 1:
        c = (b + a) // 2
        if count_less(m, c, n) < k:
            a = c
        else:
            b = c
    return a 
