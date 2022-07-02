cnt = list(range(0, 3))
num = list(map(int, input().split()))

for i in range(0, len(num)):
    cnt[i] = num.count(num[i])

if max(cnt) == 3:
    print(10000 + num[0]*1000)
elif max(cnt) == 2:
    a = cnt.index(max(cnt))
    print(1000 + num[a] * 100)
else:
    print(max(num) * 100)
