num = int(input())
list = list(0 for i in range(0, num))
for i in range(0, num):
    a, b = map(int, input().split())
    list[i] = a+b

for i in range(0, num):
    print(list[i])
