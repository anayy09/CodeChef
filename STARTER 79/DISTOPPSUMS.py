# Distinct Opposite Sums

for test in range(int(input())):
    n = int(input())
    
    for i in range(1, n//2+1):
        print(i, end=" ")
        
    for i in range(n, n//2, -1):
        print(i, end=" ")
        
    print()
