n = int(input())
a = list(map(int, input().split()))
a.sort()
s = 0
b = None
for i in a:
    if i != b:
        s += i
        b = i
print(s)
