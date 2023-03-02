# BETTER DEAL
for test in range(int(input())):
    a,b = map(int, input().split())
    p1 = 100 * ((100 - a) / 100)
    p2 = 200 * ((100 - b) / 100)
    if p2 > p1:
        print("FIRST")
    elif p1 > p2:
        print("SECOND")
    else:
        print("BOTH")
