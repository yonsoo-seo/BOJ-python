import sys

n = int(sys.stdin.readline().strip())
sum = 0
cnt = 0
for i in range(1, n+1):
    sum += i
    cnt += 1
    if sum == n:
        print(cnt)
        break
    elif sum > n:
        print(cnt-1)
        break
