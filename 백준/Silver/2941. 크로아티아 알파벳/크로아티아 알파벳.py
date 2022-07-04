import sys

li = list(sys.stdin.readline())
i = 0
cnt = 0

while i < len(li)-1:

    cnt = cnt+1

    if li[i] == 'c' and li[i+1] == '=':
        i = i+2
    elif li[i] == 'c' and li[i+1] == '-':
        i = i+2

    elif li[i] == 'd':
        if li[i+1] == 'z' and li[i+2] == '=':
            i = i+3
        elif li[i+1] == '-':
            i = i+2
        else:
            i = i+1

    elif li[i] == 'l' and li[i+1] == 'j':
        i = i+2
    elif li[i] == 'n' and li[i+1] == 'j':
        i = i+2
    elif li[i] == 's' and li[i+1] == '=':
        i = i+2
    elif li[i] == 'z' and li[i+1] == '=':
        i = i+2
    else:
        i = i+1

print(cnt)
