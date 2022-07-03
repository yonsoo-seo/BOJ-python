n = int(input())
li = [0] * n
storage = [[1], [2, 4, 8, 6], [3, 9, 7, 1],
           [4, 6], [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1]]

for i in range(n):
    a, b = map(int, input().split())
    if a % 10 == 1 or a % 10 == 5 or a % 10 == 6:
        li[i] = a % 10
    elif a % 10 == 0:
        li[i] = 10
    else:
        a = a % 10
        c = len(storage[a-1])
        li[i] = storage[a-1][b % c-1]

for i in range(n):
    print(li[i])