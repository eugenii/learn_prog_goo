# Сбалансированные подстроки.
import sys

string = sys.stdin.read().strip()
res = [0]
for i in string:
    if i == '0':
        res.append(res[-1] - 1)
    else:
        res.append(res[-1] + 1)
    if res[-1] == 0:
        idx = i
print(idx)

# for i in range(len(string)):
#     if string[i] == '0':
#         res.append(-1)
#         continue
#     res.append(1)
