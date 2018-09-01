# Exercise 3. Задача: Увеличение приоретета.


def siftup(heap, k):
    a = heap[k]
    while k > 0 and a > heap[(k - 1) // 2]:
        heap[k] = heap[(k - 1) // 2]
        k = (k - 1) // 2
    heap[k] = a
    return k

if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    # print(A)
    j = int(input())
    ind = [tuple(map(int, input().split())) for _ in range(j)]
    # print(ind)
    for i, _ in enumerate(ind):
        A[_[0] - 1] += _[1]
        # print(A[_[0] - 1])
        print(siftup(A, (_[0] - 1)) + 1)
    for z in A:
        print(z, end=' ')
