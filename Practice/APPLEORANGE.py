# Apples and Oranges

import math

for test in range(int(input())):
    n, m = map(int, input().split())
    print(math.gcd(n, m))
