def my_reverse(x):
    #переворачивает массив x
    for i in range(len(x) // 2):
        x[i], x[len(x) - 1 - i] = x[len(x) - 1 - i], x[i]
    return x

def del_element(x, a):
    #удаляет все элементы а из массива, возвращает
    # измененый массив и позицию pos, до которой
    # идет массив с выкинутыми элементами 
    pos = 0
    i = 0
    while i < len(x):
        if x[i] == a:
            pos = i
            del x[i]
        else:
            i += 1
    return x, pos 
    
    
def search_first(x, a):
    #находит индекс первого вхождения а в x
    #если такого нет, то возвращает -1 
    ans = -1
    for i in range(len(x)):
        if x[i] == a:
            ans = i
            break
    return ans

def search_last(x, a):
    #находит индекс последнего вхождения а в x
    #если такого нет, то возвращает -1 
    ans = -1
    for i in range(len(x)):
        if x[i] == a:
            ans = i
    return ans

def search_all(x, a):
    #находит все индексы вхождений а в x
    #если такого нет, то возвращает -1 
    ans = []
    for i in range(len(x)):
        if x[i] == a:
            ans.append(i)
    return ans if ans else -1

def solution(a, b):
    #решение уравнения ax + b = 0
    return -b/a if a else 'No solution'
