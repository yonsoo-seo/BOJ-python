import sys

str = input()
new_str = list(str.upper())
cnt = list(0 for i in range(len(new_str)))
num_cnt = 0

re_str = list(set(new_str))

for i in range(len(re_str)):
    cnt[i] = new_str.count(re_str[i])

for i in range(len(re_str)):
    if max(cnt) == cnt[i]:
        num_cnt += 1

if num_cnt <= 1:
    print(re_str[cnt.index(max(cnt))].upper())
else:
    print('?')