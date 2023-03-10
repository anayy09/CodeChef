# Bear and Candies 123

for test in range(int(input())):
    a, b = map(int, input().split())
    sum1, sum2 = 0, 0
    p, q = 1, 2
    turn = 1

    while True:
        if turn == 1:
            sum1 += p
            p += 2
            if sum1 > a:
                print("Bob")
                break
            turn = 2
        else:
            sum2 += q
            q += 2
            if sum2 > b:
                print("Limak")
                break
            turn = 1
            
