'''
timer(spam, 1, 2, a=3, b=4, _reps=1000) вызывает и измеряет
время работы функции spam(1, 2, a=3) _reps раз,
и возвращает общее время, затраченное на все вызовы,
с результатом вызова испытуемой функции;

best(spam, 1, 2, a=3, b=4, _reps=50) многократно
вызывает функцию timer, чтобы исключить влияние флуктуаций
в нагрузке на систему, и возвращает лучший результат из
серии по _reps испытаниям
'''

import time, sys

if sys.platform[:3] == 'win':
    timefunc = time.clock
else:
    timefunc = time.time

def trace(*args): pass

def timer(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 1000)

    trace(func, pargs, kargs, _reps)
    repslist = range(_reps)

    start = timefunc()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timefunc() - start
    return (elapsed, ret)

def best(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 50)
    best = 2 ** 32
    for i in range(_reps):
        (time, ret) = timer(func, *pargs, _reps = 1, **kargs)
        if time < best: best = time
    return(best, ret)


    

