def minmax(test, *args):
    res = args[0]
    for i in args[1:]:
        if test(i, res):
            res = i
    return res

def lessthen(x, y): return x < y
def morethen(x, y): return x > y

if __name__ == '__main__':
    print(minmax(lessthen, 1, 2, 3, 4, 5, 6, 7, 8))
    print(minmax(morethen, 1, 2, 3, 4, 5, 6, 7, 8))
