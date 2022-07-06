import sys

n = int(sys.stdin.readline())
sum = 0
li = [0] * n
i = 0
for _ in range(n):
    li[i] = int(sys.stdin.readline())
    i += 1
    if li[i-1] == 0:
        i = i-2
        li[i] = 0

for i in range(n):
    sum += li[i]

print(sum)