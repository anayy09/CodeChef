# Chef and Dolls

for test in range(int(input())):
    n = int(input())
    l = []
    for i in range(n):
        l.append(int(input()))
    for j in l:
        if l.count(j)%2 == 1:
            print(j)
            break
