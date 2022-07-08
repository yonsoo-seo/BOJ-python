import sys
n = [int(sys.stdin.readline().strip()) for _ in range(10)]


sum = 0

for i in range(10):
    sum += n[i]
    if sum >= 100:
        if sum == 100:
            print(100)
            break
        else:
            if abs(100-sum) == abs(100-(sum-n[i])) or abs(100-sum) <= abs(100-(sum-n[i])):
                print(sum)

                break
            else:
                print(sum-n[i])
                break

    else:
        if i == 9:
            print(sum)
