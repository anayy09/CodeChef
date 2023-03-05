# Adjacent Sum Parity

for test in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    if sum(b) % 2 == 0:
        print("YES")
    else:
        print("No")
