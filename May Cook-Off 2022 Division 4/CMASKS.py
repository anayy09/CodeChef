# Chef and Masks
for test in range(int(input())):
    x, y = map(int, input().split())
    if x * 100 >= y * 10:
        print("Cloth")
    else:
        print("Disposable")
