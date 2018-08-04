'''def min1(*args):
    res = args[0]
    for i in args[1:]:
        if i < res:
            res = i
    return res

def min2(first, *rest):
    for i in rest:
        if i < first:
            first = i
    return first

def min3(*args):
    f = list(args)
    f.sort()
    return f[0]

print(min1(3, 4, 1, 5))
print(min2('bb', 'aa'))
print(min3([2, 2], [1,1], [3,3]))'''

def intersect(*args):
    res = []
    for i  in args[0]:
        for other in args[1:]:
            if i not in other: break
        else:
            res.append(i)
    return res


def union(*args):
    res = []
    for seq in args:
        for i in seq:
            res.append(i)
    return res


    



    
            
