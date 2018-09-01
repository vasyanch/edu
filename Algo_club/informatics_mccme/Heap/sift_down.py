# Exercise 4. Задача: Уменьшение приоретета.


def siftdown(mas, k):
    while (2*k + 1) < len(mas):
        j = k
        if mas[j] < mas[(2*k + 1)]:
            j = 2 * k + 1
        if (2*k + 2) < len(mas) and mas[j] < mas[(2*k + 2)]:
            j = 2 * k + 2
        if k == j:
            break
        else:
            mas[k], mas[j] = mas[j], mas[k]
            k = j
    return k
    

if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    # print(A)
    l = int(input())
    ind = [tuple(map(int, input().split())) for _ in range(l)]
    # print(ind)
    for i, _ in enumerate(ind):
        A[_[0] - 1] -= _[1]
        # print(A[_[0] - 1])
        print(siftdown(A, (_[0] - 1)) + 1)
    for z in A:
        print(z, end=' ')
