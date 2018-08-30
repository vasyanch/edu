# Exercise 5(E). Задача: Приорететная очередь  с удалением(очередь с приорететом).


def siftup(mas, i):
    while i > 0 and mas[i] > mas[(i - 1) // 2]:
        mas[(i - 1) // 2], mas[i] = mas[i], mas[(i - 1) // 2]
        i = (i - 1) // 2
    return i


def siftdown(mas, i):
    while (2 * i + 1) < len(mas):
        j = i
        if mas[j] < mas[(2 * i + 1)]:
            j = 2 * i + 1
        if (2 * i + 2) < len(mas) and mas[j] < mas[(2 * i + 2)]:
            j = 2 * i + 2
        if i == j:
            break
        else:
            mas[i], mas[j] = mas[j], mas[i]
            i = j
    return i


def extract_max(mas):
    if len(mas) == 1:
        return 0, mas.pop()
    else:
        m = mas[0]
        mas[0] = mas.pop()
        return siftdown(mas, 0) + 1, m


def insert(mas, x, n):
    if len(mas) < n:
        mas.append(x)
        return siftup(mas, len(mas) - 1) + 1
    else:
        return -1


def del_(mas, i):
    if i <= 0 or i > len(mas):
        return -1
    elif i == len(mas):
        return mas.pop()
    else:
        a = mas[i - 1]
        mas[i - 1] = mas[-1]
        mas.pop()
        siftdown(mas, i - 1)
        siftup(mas, i - 1)
        return a


if __name__ == '__main__':
    N, M = tuple(map(int, input().split()))
    A = []
    for _ in range(M):
        req = tuple(map(int, input().split()))
        if req[0] == 1:
            if len(A) == 0:
                print(-1)
            else:
                ans = extract_max(A)
                print(ans[0], ans[1])
        if req[0] == 2:
            print(insert(A, req[1], N))
        if req[0] == 3:
            print(del_(A, req[1]))
            # print(A)
    for _ in A:
        print(_, end=' ')
