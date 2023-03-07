# Break the Stick

for test in range(int(input())):
    n,x = map(int, input().split())
    if n > x:
        if n % 2 == 0 and x % 2 == 0:
            print("YES")
        elif n % 2 == 0 and x % 2 != 0:
            print("YES")
        elif n % 2 != 0 and x % 2 != 0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
