from math import sqrt
from fractions import Fraction
from math import sqrt

def num_of_d(a):
    ''' Возвращает количество натуральных делителей числа а'''
    ch = 2 
    if a == 1:
        return 1 
    else:
        for i in range(2, int(sqrt(a)) + 1):
            if a % i == 0:
                ch += 2
    return ch


def bin_k(n, k):
    ''' Возвращает биномиальный коэффициент'''
    if k > n: return 0
    if k > n // 2: k = n - k
    if k == 0: return 1
    if k == 1: return n
    ans = 1
    for i in range(n, k, -1):
        ans *= Fraction(i, i - k)
    return ans

