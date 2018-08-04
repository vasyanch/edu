with open('dataset_24465_4.txt') as in_:
    e = in_.read().splitlines(); e.reverse()
with open('out.txt', 'w') as out:
    for i in e:
        out.write(i + '\n')
    


    
