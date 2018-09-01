a = int(input('Вместимость 1-го кувшина\n'))
b = int (input('Вместимость 2-го кувшина\n'))
out_volume = int (input('Искомый объем\n'))

d = max(a, b)
e = min(a, b)
if out_volume > d: 
    print ('Такой объем не поместиться ни в одном из кувшинов')
elif out_volume == d:
    print ('Fill #1:%s  #2:0' % d)
elif out_volume == e:
    print ('Fill #1:0 #2:%s' % e)
else:
    print('Bye')
    



