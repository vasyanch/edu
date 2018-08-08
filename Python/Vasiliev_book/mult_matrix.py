'''
    В данном коде реализованы три функции:
        rand_matrix(n,m)    - инициализирует  и возвращает
        матрицу n на m, представленную в виде вложенных списков.
        unit_matrix(n)      - возвр. единичную матрицу размера n.
        mult_matrix(A1, A2) - возвр. произведение матриц A1 и A2.
        show_matrix(A)      - выводит в консоль матрицу в
        мат-ом виде.
'''

from random import *

def rand_matrix(n, m):
    A = [[randint(0, 9) for j in range(m)] for i in range(n)]
    return A

def unit_matrix(n):
    A = [[int(i == j) for j in range(n)] for i in range(n)]
    return A

def mult_matrix(A, B):
    n = len(A)           #кол-во строк в матрице А
    if n == len(B[0]):
        C = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    C[i][j] += A[i][k] * B[k][j]
        return C
    else:
        print(''''Sorry, number of string in A must equal
              number of column in B. Try again.''')

def show_matrix(a):
    for i in a:
        for j in i:
            print(j, end = ' ')
        print()

if __name__ == '__main__':
    seed(2014)
    A = rand_matrix(3, 5)
    print('Список:', A)
    print('Эта же матрица:')
    show_matrix(A)
    E = unit_matrix(4)
    print('Единичная матрица:')
    show_matrix(E)
    A1 = rand_matrix(3,3)
    A2 = rand_matrix(3,3)
    print('Первая матрица:')
    show_matrix(A1)
    print('Вторая матрица:')
    show_matrix(A2)
    print('Произведение матриц:')
    show_matrix(mult_matrix(A1, A2))
    
