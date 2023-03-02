# Add smallest prime factor

for test in range(int(input())):
    x, y = map(int, input().split())
    if x % 2 == 0:
        pF = 2
    elif x % 3 == 0:
        pF = 3
    else:
        pF = x
    x += pF
    d = y - x
    ans = d // 2
    if d % 2 != 0:
        ans += 1
    print(ans + 1)
