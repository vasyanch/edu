# Exercise 3. Задача: Извлечение максимального. Не проходит по времени, лимит 1 сек.,
# программа отрабатывает за 1.107 сек. Пчм так - хз(


def siftdown(massif, i, s):
    while (2*i + 1) < s:
        j = i
        if massif[i] < massif[(2*i + 1)]:
            j = 2*i + 1
        if (2*i + 2) < s and massif[j] < massif[(2*i + 2)]:
            j = 2*i + 2
        if i == j:
            break
        else:
            massif[i], massif[j] = massif[j], massif[i]
            i = j
    return i


def extract_max(massif, s):
    m = massif[0]
    massif[0] = massif[s - 1]
    return siftdown(massif, 0, s - 1) + 1, m

size = int(input())
A = [int(_) for _ in input().split()]
while size > 1:
    ans = extract_max(A, size)
    print(ans[0], ans[1])
    size -= 1
