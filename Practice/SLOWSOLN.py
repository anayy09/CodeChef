# Slow Solution

for test in range(int(input())):
    mT,mN,sN = map(int,input().split())
    res = 0
    while(mT > 0):
        n = min(mN,sN)
        res += n * n
        mT -= 1
        sN -= n
    print(res)
