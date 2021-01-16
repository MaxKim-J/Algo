# 이분탐색 안써도 풀리겠구나 => 를 생각해냈어야함
#! 이분탐색 발적화 문제

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
finds = list(map(int, input().split()))

cards.sort()
sorted_finds = sorted(finds)

start_memo = 0
result = dict()

for find in sorted_finds:
    prev_start = start_memo
    start = start_memo
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if cards[mid] <= find:
            start = mid + 1
            start_memo = mid
        else:
            end = mid - 1
    if cards[start_memo] == find:
        result[find] = 1
        max_idx, min_idx = start_memo + 1, start_memo - 1
        while (max_idx < N) and (cards[max_idx] == find):
            result[find] += 1
            mad_idx += 1
        while (min_idx > -1) and (cards[min_idx] == find):
            result[find] += 1
            min_idx -= 1
    else:
        result[find] = 0
        start_memo = prev_start

for find in finds:
    print(result[find], end=' ')

'''
걍 순회로도 풀림 => 오히려 O(2n)이 더 빠른 경우

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
'''
