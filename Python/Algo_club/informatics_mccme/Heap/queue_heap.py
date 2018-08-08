# Exercise 4(D). Задача: Приорететная очередь(очередь с приорететом).


def siftup(massif, i):
    while i > 0 and massif[i] > massif[(i - 1) // 2]:
        massif[(i - 1) // 2], massif[i] = massif[i], massif[(i - 1) // 2]
        i = (i - 1) // 2
    return i


def siftdown(massif, i):
    while (2*i + 1) < len(massif):
        j = i
        if massif[i] < massif[(2*i + 1)]:
            j = 2*i + 1
        if (2*i + 2) < len(massif) and massif[j] < massif[(2*i + 2)]:
            j = 2*i + 2
        if i == j:
            break
        else:
            massif[i], massif[j] = massif[j], massif[i]
            i = j
    return i 


def extract_max(massif):
    if len(massif) == 1:
        return 0, massif.pop()
    else:
        m = massif[0]
        massif[0] = massif.pop()
        return siftdown(massif, 0) + 1, m


def insert(massif, x, n):
    if len(massif) < n:
        massif.append(x)
        return siftup(massif, len(massif) - 1) + 1
    else:
        return -1
         

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
        # print(A)
    for _ in A:
        print(_, end=' ')
