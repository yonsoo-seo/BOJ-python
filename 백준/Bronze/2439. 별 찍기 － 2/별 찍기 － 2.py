n = int(input())

for i in range(1, n+1):
    if i > 1:
        print()
    for j in range(n-i):
        print(' ', end='')
    for k in range(i):
        print('*', end='')