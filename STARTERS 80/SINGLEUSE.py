# Single-use Attack

for test in range(int(input())):
    h, x, y = map(int, input().split())
    h -= y
    if h % x == 0:
        print(1 + h//x)
    else:
        print(2 + h//x)
