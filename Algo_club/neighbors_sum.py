def new_m(x):
    # преоб. массив так, что на месте x[i] находится
    # сумма его соседей в исходном массиве 
    a = x[0]
    for i in range(1, len(x) -1):
        b = x[i]
        x[i] = a + x[i + 1]
        a = b
    return x

def dispersion(x):
    #возвращает дисперсию массива x 
    it = iter(x)
    a, b, n = 0, 0, len(x)
    for i in it:
        a += i ** 2
        b += i
        disp = a/n - (b/n) ** 2
    return disp 

def polynomial(x):
# x = [x0, a_0, ... a_(n-2), a_(n-1)], точка x0  и коэффициенты
#при степенях аргумента полинома степени n  = len(x) - 1
# возвращает значение полинома в точке x0
    it = iter(x)
    b = next(it)
    z = next(it)
    z_ = 0
    c = 1
    i = 0
    for a in it:
        i += 1
        z_ += a * c * i
        c *= b
        z += a * c
    return z, z_

def polynomial_(x):
# x = [x0, a_(n-1), a_(n-2), ... a_0], точка x0  и коэффициенты
#при степенях аргумента полинома степени n  = len(x) - 1
# возвращает значение полинома в точке x0
    it = iter(x)
    b = next(it)
    z = 0
    z_ = 0
    for a in it:
        z_ = z_ * b + z
        z = (z * b + a)
    return z, z_
