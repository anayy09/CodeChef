# Lucky Number Game
import math

def solve(na, nb, c, a, b):
    if nb > na:
        return "BOB"
    else:
        return "ALICE"

for test in range(int(input())):
    n, a, b = map(int, input().split())
    v = list(map(int, input().split()))
    na = 0
    nb = 0
    c = 0
    for i in range(n):
        if v[i] % a == 0:
            nb += 1
        elif v[i] % b == 0:
            na += 1
        if v[i] % a == 0 and v[i] % b == 0:
            c += 1
    print(solve(na, nb, c, a, b))
