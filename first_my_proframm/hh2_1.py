def dec(step, a):
    global remember
    global k
    if (step < n) and (step >= 0):
        for i in range(step, k):
            if (a[step] - 1 >= a[i] + 1):
                remember = remember + 1
                a[step] = a[step] - 1
                a[i] = a[i] + 1
                print(a)
                dec(step + 1, a)
                dec(step, a)
                dec(step - 1, a)
                break

n = int(input('Введите n='))
k = int(input('Введите k='))
a = [1] * k
a[0] = n - k + 1
remember = 1
dec(0, a)
print (remember,"cпособов(а) представить n в в виде k слагаемых.")
