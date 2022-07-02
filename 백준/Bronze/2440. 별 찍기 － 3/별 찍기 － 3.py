n = int(input())

for i in range(0, n):
    if i > 0:
        print()
    for j in range(i, n):
        print('*', end='')