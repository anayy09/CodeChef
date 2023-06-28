# Equal Difference
for test in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    if n == 2:
        print("0")
    elif n == 1:
        print("0")
    else:
        un = {}
        for j in range(n):
            if arr[j] in un:
                un[arr[j]] += 1
            else:
                un[arr[j]] = 1

        max_freq = 0
        for key in un:
            if un[key] > max_freq:
                max_freq = un[key]

        if max_freq == 1:
            print(n - 2)
        else:
            print(n - max_freq)
