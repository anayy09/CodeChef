# Chef and Gym
for test in range(int(input())):
    x, y, z = map(int, input().split())
    if z > x and z - x >= y:
        print(2)
    elif z >= x and z - x < y:
        print(1)
    else:
        print(0)
