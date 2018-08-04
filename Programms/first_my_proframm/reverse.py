def reverse(text):
    
    lst = []
    lst_ = []
    
    for i in text:
        lst.append(i)
        
    t = 0     
    for i in range(len(lst)):
        t = len(lst) - 1 - i
        lst_.append(lst[t])
    a = ''   
    for i in range(len(lst_)):
        a = a +  "".join(lst_[i])
    print (a)    
    return a    
       
reverse('vasa')

