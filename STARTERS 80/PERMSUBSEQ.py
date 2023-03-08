# Permutation Subsequence

from collections import defaultdict as dd

for test in range(int(input())):
    n = int(input())
    a = dd(int)
    MOD = int(1e9 + 7)

    for x in map(int, input().split()):
        a[x] += 1
    
    pss = 0
    pre = 1
    
    for i in range(1, n+1):
        temp = pre * a[i]
        temp %= MOD
        pss += temp
        pre = temp
        pss %= MOD

    print(pss)
