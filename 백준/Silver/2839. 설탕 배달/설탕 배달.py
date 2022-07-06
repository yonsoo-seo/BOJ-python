import sys

n = int(sys.stdin.readline())

if n % 5 == 0:
    print(n//5)
else:
    cnt = 0
    while n > 0:
        n -= 3
        cnt += 1
        if n % 5 == 0:
            cnt += n//5
            print(cnt)
            break
        elif n % 3 == 0 and n//5 < 1:
            cnt += n//3
            print(cnt)
            break
        elif n == 1 or n == 2:
            print(-1)
            break
