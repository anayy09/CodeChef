# ATM Machine

for test in range(int(input())):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = ''
    for i in a:
        if i <= k:
            ans += '1'
            k -= i
        else:
            ans += '0'
    print(ans)
