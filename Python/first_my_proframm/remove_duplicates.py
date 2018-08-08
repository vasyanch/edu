def remove_duplicates(lst):
    a = []
    lst.sort()
    a = lst
    tsl = []
    t = 0
    for i in a:
        if t == i:
            tsl.append(t)
        else:
            if t < i:
                while t < i:
                    t = t + 1
                tsl.append(t)
                t = t + 1               
    return tsl
print (remove_duplicates([3, 3, 5, 6, 2, 1, 7, 5]))
