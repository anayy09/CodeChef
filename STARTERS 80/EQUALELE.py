# Equal Elements

for test in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    m = {}
    for i in range(n):
        if a[i] in m:
            m[a[i]] += 1
        else:
            m[a[i]] = 1
            
    maxee = 0
    for i in m:
        maxee = max(maxee, m[i])
        
    if maxee != 0:
        print(n - maxee)
    else:
        print(n - 1)
