# Encoding Message

for test in range(int(input())):
    n = int(input())
    s = input()
    a = list(s)
    sn = ''
    for i in range(1,n,2):
        s1 = a[i-1]
        a[i-1] = a[i]
        a[i] = s1
    for i in range(n):
        if ord(a[i]) <= 110:
            diff = 97 - ord(a[i])
            add = 122 + diff
            a[i] = chr(add)
            sn += a[i]
        elif ord(a[i]) > 110:
            diff = 122 - ord(a[i])
            add = 97 + diff
            a[i] = chr(add)
            sn += a[i]
    print(sn)
