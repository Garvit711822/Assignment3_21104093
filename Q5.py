n = 6
for i in range(n):
    for j in range(i):
        print(' ', end='')
    for k in range(2 * (n-i)-1):
        print(chr(65 + k), end='')
    print()