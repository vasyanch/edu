'''def  adder(good, bad, ugly):
    spisok = list((good, bad, ugly))
    summ = spisok[0]
    for i in spisok[1:]:
        summ += i

    return summ

print(adder('Vasya', 'LOVE', 'Alla'))
print(adder([], [234,567], ['asdf', 'hbdfb']))
print(adder(1.34567, 1.567890, 6.789234))
'''

def  adder_dict(**args):
    spisok = list(args.keys())  #можно делать список из значений
    summ = args[spisok[0]]      #словаря args методом args.values()
    for key in spisok[1:]:
        summ += args[key]

    return summ




   

