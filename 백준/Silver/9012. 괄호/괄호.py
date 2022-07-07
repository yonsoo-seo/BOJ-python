import sys

n = int(sys.stdin.readline())
li = list(sys.stdin.readline().strip() for _ in range(n))
cnt = [0] * 2
ans = [0] * n

for i in range(n):
    cnt[0] = cnt[1] = 0
    ans[i] = 'YES'

    for j in range(len(li[i])):
        if li[i][j] == '(':
            cnt[0] += 1

        elif li[i][j] == ')':
            cnt[1] += 1

        if cnt[0] < cnt[1]:
            ans[i] = 'NO'

            break

    if cnt[0] != cnt[1]:
        ans[i] = 'NO'


print(*ans, sep='\n')
