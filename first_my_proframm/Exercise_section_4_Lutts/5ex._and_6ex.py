def copyDict(a):
    x = {}
    for key in a:
        x[key] = a[key]
    return x


    

def addDict(a, b):
    x = {}
    for i in (a, b):
        for key in i:
            x[key] = i[key]
    return x



def addDict_2(a, b):
    if type(a) == type({}):
        x = {}
        for i in (a, b):
            for key in i:
                x[key] = i[key]
    elif type(a) == type([]):
        x = a + b
    return x
