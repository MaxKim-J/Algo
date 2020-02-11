# 배열을 몇번이나 돌게 될지 생각하기

import sys

data_num = sys.stdin.readline()
data_list = list(map(int, sys.stdin.readline().split()))

find_num = sys.stdin.readline()
find_list = list(map(int, sys.stdin.readline().split()))

data_dict = {}
for n in data_list:
    try:
        data_dict[n] += 1
    except:
        data_dict[n] = 1

answer = []
for m in find_list:
    try:
        answer.append((data_dict[m]))
    except:
        answer.append(0)

for i in answer:
    print(i, end=' ')
