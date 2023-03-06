# Chef Diet

for test in range(int(input())):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    p = 0
    f = 1
    for i in range(n):
        p += a[i] - k
        if p < 0:
            f = 0
            break
    if f == 1:
        print("YES")
    else:
        print("NO ",i+1)
