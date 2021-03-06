'''
    Фун. D(f) находит производную фун. f численым методом
    и возвращает ее в виде f'(x, dx).
    Фун. show сравнивает численное значение производной
    со значенем полученым из аналитической формулы для
    нескольких зачений аргумента x,
    для двух часных случаев f1 and f2.
'''

def D(f):
    def df(x, dx = 0.001):
        return (f(x+dx) - f(x))/dx
    return df

def f1(x):
    return x**2

def f2(x):
    return 1/(x+1)

def show(F, N, X, dx, f):
    for i in range(N+1):
        x  = i*X/N
        print(F(x), F(x, dx), f(x), sep = '\t')
        
print('Производная x**2 = 2*x:')
show(D(f1), 10, 2, 0.01, lambda x: 2*x)
print('Производная 1/(x+1) = -1/(x+1)**2:')
show(D(f2), 10, 2, 0.01, lambda x: -1/(1+x)**2)    
