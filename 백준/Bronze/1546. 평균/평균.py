import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
a = max(num)
avg = 0

for i in range(n):
    num[i] = num[i]/a*100
    avg += num[i]

print(avg/n)
