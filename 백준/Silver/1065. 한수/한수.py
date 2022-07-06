import sys

n = int(sys.stdin.readline())
f = s = t = 0
li = [0] * 3
cnt = 0

if n < 100:
    print(n)
else:
    for i in range(100, n+1):
        f = i//100
        s = i//10 - f*10
        t = i-(f*100 + s*10)

        if f-s == s-t:
            cnt += 1
    print(cnt+99)
