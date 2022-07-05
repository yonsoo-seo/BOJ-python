import sys

n = int(sys.stdin.readline().strip())
a = 1
cnt = 0

if n < 5:
    print(cnt)
else:
    for i in range(1, n+1):
        a *= i

    og = a

    while True:
        check = og % 10
        if check == 0:
            og = og // 10
            cnt += 1
        elif check != 0:
            print(cnt)
            break
