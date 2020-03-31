# 해시테이블 백준 7615번
# 메모리 초과됨;; 좀더 연구해보자

import sys
import math

commands = int(sys.stdin.readline())
for command in range(commands):
    a, b, x, n, c, d, m = map(int, sys.stdin.readline().split())
    modulo = b % m
    min_num = math.ceil((c - modulo) / a)
    max_num = math.trunc((d - modulo) / a)
    if min_num <= x:
        min_num = x
    if max_num >= x + n:
        max_num = x + n
    result = range(min_num, max_num+1)
    sys.stdout.write(f"{len(result)}\n")
