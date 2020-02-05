# 그냥 무식한 카운팅 정렬로 풀기

import sys

N = int(sys.stdin.readline())
series = [0] * 10001

for i in range(N):
    a = int(sys.stdin.readline())
    series[a] = series[a] + 1

for b in range(len(series)):
    if series[b] != 0:
        for c in range(series[b]):
            print(b)
