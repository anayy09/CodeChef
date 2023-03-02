# One Stone or Two Stones

# cook your dish here
for test in range(int(input())):
    x, y = map(int, input().split())

    if x == y:
        if x % 2 != 0:
            print("CHEF")
        else:
            print("CHEFINA")
        continue
    d = abs(x-y)

    if d >= 2 and x > y:
        print("CHEF")
        continue

    elif d >= 2 and x < y:
        print("CHEFINA")
        continue

    if x % 2 != 0 and x > y:
        print("CHEFINA")
        continue

    elif x % 2 == 0 and x > y:
        print("CHEF")
        continue

    elif y % 2 == 0 and x < y:
        print("CHEF")
        continue

    elif y % 2 != 0 and x < y:
        print("CHEFINA")
        continue
