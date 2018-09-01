'''
mydir.py:выводит содержимое пространства имен других модулей
'''

seplen = 60
c = '-'

def listing(module, verbose = True):
    sepline = c * seplen
    if verbose:
        print(sepline)
        print('name:', module.__name__ + ',', 'file', module.__file__)
        print(sepline)

    count = 0
    for atr in module.__dict__:
        print('%02d) %s' % (count, atr), end = ' ')
        if atr.startswith('__'):
            print('<built-in name>')
        else:
            print(getattr(module, atr))
        count += 1
    if verbose:
        print(sepline)
        print(module.__name__, 'has %d names' % count)
        print(sepline)


if __name__ == '__main__':
    import mydir
    listing(mydir)

        
