'''
Функции, которые определяют является ли целое положительное
число простым.
'''

def prime(y):
    if not y > 1:
        print(y, 'not prime')
    else:
        x = y // 2
        while 1 < x:
            if y % x == 0:
                print(y, 'has factor', x)
                break
            x -=1
        else:
            print(y, 'is prime')

print('Run the prime:')
prime(13)
prime(14.00)
prime(45.78)
prime(-77)
prime(-88)
prime(0)
print('')


def prime_2(y):
    if not y > 1:
        print(y, 'not prime')
    elif  y != int(y):
        print(y, 'not prime')
    else:
        x = y // 2
        for i in range(x, 1, -1):
            if y % i == 0:
                print(y, 'has factor', i)
                break
        else:
            print(y, 'is prime!')


print('Run the prime_2:')
prime_2(13)
prime_2(14)
prime_2(-77)
prime_2(-88)
prime_2(0)
prime_2(13.67)
prime_2(2.5)




    
