n = int(input())

for i in range(n+1):
    if i > 1:
        print()
    for j in range(0, i):
        print('*', end='')
