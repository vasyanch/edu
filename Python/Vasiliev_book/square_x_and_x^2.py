'''
    Данный код выполняет вычисление площади фигуры ограниченной
    графиками y = x and y = x**2 и возвращает ее в виде результата.
    Используется методы Монте-Карло, имеющий отношение к теории
    вероятностей. Данная задача имеет точное решение через
    интеграл разности этих функций.
    Фун. graphs строит графики этих функций в пределах 0 <= x <= 1.5.
    Для построения ее нужно вызвать: graph().
'''

from matplotlib import pyplot as plt


def graphs():
    x = [i / 10 for i in range(16)] 
    plt.plot(x, [x**2 for x in x], label = 'x**2')
    plt.plot(x, [x for x in x], label = 'x')
    plt.legend()
    plt.grid(True)
    plt.show()

    
n = 500
pts = 0
dz = 1/n
i = 0
while i <= n:
    x = dz * i
    j = 0
    while j <= n:
        y = dz * j
        if x ** 2 <= y <= x:
            pts += 1
        j += 1
    i += 1
s = pts/(n + 1) ** 2
print('Площадь равна s = {}'.format(s))
