# Running Comparison

for test in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    h = 0
    for j in range(n):
        if a[j] <= 2 * b[j] and b[j] <= 2 * a[j]:
            h += 1
    print(h)
