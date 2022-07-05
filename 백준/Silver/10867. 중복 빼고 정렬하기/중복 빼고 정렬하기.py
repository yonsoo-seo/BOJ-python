import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

li = set(num)
li = list(li)
li.sort()


print(*li, sep='\n')
