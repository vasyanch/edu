def censor(text, word):
    lst = text.split()
    l = len(word)
    a = ' '
    for i in range(len(lst)):
        if lst[i] == word:
            lst[i] = '*' * l
    for i in lst:
        a =  a + ''.join(i) + ' '
    return a
    
print (censor('vasa alla vasa alla', 'alla'))

    
    
