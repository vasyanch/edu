'''
    Задача: найти количество  натуральных делителей биномиального
    коэффициента. На вход дается два числа  k and n.
'''
from math import sqrt
from fractions import Fraction
from math import sqrt


def prime_in(n, p):
    ''' возвращает степень в которой простое число p входит
        в n! при разложении в произведение степеней простых чисел''' 
    ch = 0
    q = n // p
    while q >= 1:
        ch += q
        q = q // p 
    return ch


def prime_gen(n):
    ''' возвращает список простых чисел не больших n'''
    prime_lst = [2]
    for i in range(3, n + 1, 2):  # простые только нечетные 
        if i > 10:
            if i % 2 == 0 or i % 10 == 5: # проверка деления на 2 и на 5 
                continue
        for j in prime_lst: # если есть делители то они точно делятся на меньшие простые 
            if j * j > i: # максимальный делитель не может быть больше корня
                prime_lst.append(i)   
                break
            if i % j == 0:
                break
        else:
            prime_lst.append(i)
    #print(prime_lst)
    return prime_lst 


def num_dividers_bin(n, k):
    ''' возвращает количество натуральных делители биномиального
    коэффициента.'''
    prime = prime_gen(n)
    lst_of_powers = [1] * len(prime)
    #print(lst_of_powers)
    for i, v in enumerate(prime):  
        #print(i, v)
        lst_of_powers[i] = prime_in(n, v) - prime_in(k, v) - prime_in(n - k, v) + 1
    #print(lst_of_powers)
    ans = 1
    for _ in lst_of_powers:
        ans *= _
    return ans


if __name__ == '__main__':
    k_, n_ = map(int, input().split())
    print(num_dividers_bin(n_, k_))

