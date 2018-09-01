def  adder(*a):
    sum = a[0]
    for i in a[1:]:
        sum += i

    return sum

print(adder('Vasya', 'LOVE', 'Alla'))
print(adder([], [234,567], ['asdf', 'hbdfb']))
print(adder(1.34567, 1.567890, 6.789234))


   

