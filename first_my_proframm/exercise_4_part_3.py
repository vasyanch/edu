E = [1, 2, 4, 8, 16, 32, 64]
Y = 5
#found = False
#i = 0
'''while i < len(L):
    if 2 ** x == L[i]:
        print('at index', i)
        break
    i +=1
else:
    print(x, 'not found')'''

#if found:
 #   print('at index', i)
#else:
 #   print(x, 'not found')

'''for i in L:
    if 2 ** x == i:
        print('at index', L.index(i))
        break
else:
    print(x, 'not found')'''

'''if 2 ** x in L:
    print(2 ** x, 'was found at index', L.index(2 ** x))
else:
    print(x, 'not found')'''

L = []
_x = 5
for i in range(7):
    L.append(2 ** i)
if 2 ** _x in L:
    print(2 ** _x, 'was found at index', L.index(2 ** _x))
else:
    print(_x, 'not found')
__all__ = ['E', 'Y', '_x']


    
