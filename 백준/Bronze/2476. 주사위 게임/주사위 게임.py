n = int(input())
score = list(0 for i in range(0, n))

for i in range(n):
    a, b, c = map(int, input().split())
    if a == b == c:
        score[i] = 10000 + a*1000
    elif a == b or b == c:
        score[i] = 1000 + b*100
    elif a == c:
        score[i] = 1000 + a*100
    else:
        if a >= b and a >= c:
            score[i] = a*100
        elif b >= a and b >= c:
            score[i] = b*100
        elif c >= a and c >= b:
            score[i] = c*100

print(max(score))