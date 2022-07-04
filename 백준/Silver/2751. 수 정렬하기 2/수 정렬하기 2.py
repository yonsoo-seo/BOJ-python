import sys

n = int(sys.stdin.readline())
li = [0]*n
for i in range(n):
    li[i] = int(sys.stdin.readline())

li.sort()

for i in range(n):
    print(li[i])