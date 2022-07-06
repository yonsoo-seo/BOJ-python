a, b = map(int, input().split())
li = [0] * 1000
k = 0
sum = 0

for i in range(1, 1001):
    if k > 999:
        break
    for j in range(1, i+1):
        if k > 999:
            break
        li[k] = i
        k = k+1

for i in range(a-1, b):
    sum += li[i]


print(sum)
