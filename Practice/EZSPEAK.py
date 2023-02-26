# Easy Pronounciation

for test in range(int(input())):
    n = int(input())
    word = input()
    vowels = 'aeiou'
    count = 0
    for letter in word:
        if letter not in vowels:
            count += 1
        else:
            count = 0
        if count == 4:
            print('NO')
            break
    else:
        print('YES')
