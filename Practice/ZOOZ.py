# Zero Ones Equals One Zeros

for test in range(int(input())):
    
    n = int(input())
    
    if n % 2 == 0:
        middle_zeros = '0' * (n - 2)
        res = '1' + middle_zeros + '1'
        
    else:
        middle_zero_count = n // 2
        middle_zeros = '0' * middle_zero_count
        res = middle_zeros + '1' + middle_zeros
        
    print(res)
