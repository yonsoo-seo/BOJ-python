h, m = map(int, input().split())
plus_m = int(input())

m = plus_m + m

if m >= 60:

    while(m >= 60):
        h = h+1
        m = m-60

if h > 23:
    h = h-24

print(h, m)