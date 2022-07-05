n = int(input())
li = [0]*n
check = [0]*n
c = 0

for i in range(n):
    li[i] = input()

for i in range(n):
    for j in range(len(li[i])):
        if len(li[i]) < 3:
            break
        for k in range(j+2, len(li[i])):
            if li[i][j] == li[i][k]:
                if li[i][k-1] == li[i][k]:
                    break
                else:
                    check[i] += 1
                    break
            else:
                continue

for i in range(n):
    if check[i] == 0:
        c = c+1


print(c)
