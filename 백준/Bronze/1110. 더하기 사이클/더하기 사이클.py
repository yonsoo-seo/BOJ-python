n = int(input())
og = n
cnt = 0

while cnt < 100:

    if n == 0:
        print(1)
        break

    if n < 10:
        n = n*10

    if cnt >= 2 and og == n:
        break

    cnt += 1

    temp1 = n//10
    temp2 = n % 10

    if temp2 == 0:
        if cnt > 1 and temp1 == og:
            cnt = cnt-1
            break

        cnt += 1
        n = temp1*10 + temp1
    else:
        temp3 = (temp1+temp2) % 10
        n = temp2*10 + temp3


if n != 0:
    print(cnt)
