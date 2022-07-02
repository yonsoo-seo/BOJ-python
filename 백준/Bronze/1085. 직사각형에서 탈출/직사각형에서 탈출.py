x, y, w, h = map(int, input().split())
list = list(range(0, 4))
list[0] = abs(x - 0)
list[1] = abs(y - 0)
list[2] = abs(w - x)
list[3] = abs(y - h)

print(min(list))