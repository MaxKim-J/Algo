# BFS로도 가능하긴 한데 DP를 적극 이용하면 이런식..
# 하향식 완전탐색 -> 하향식 캐싱 -> 상향식 DP

import itertools

n = int(input())
lst = list(map(int, input().split()))

dp = [[[-1 for _ in range(61)] for _ in range(61)] for _ in range(61)] # 캐싱의 목적으로

def go(a, b, c):
    if a < 0:
        return go(0, b, c)
    if b < 0:
        return go(a, 0, c)
    if c < 0:
        return go(a, b, 0)
    if a == 0 and b == 0 and c == 0:
        return 0
    if dp[a][b][c] != -1: # DP에다가 캐싱 => 패턴화하는 방식ㅎ
        return dp[a][b][c]

    dp[a][b][c] = 999999999

    for case in list(itertools.permutations([1, 3, 9])):
        dp[a][b][c] = min(dp[a][b][c], go(a - case[0], b - case[1], c - case[2]))
        # 현재 있는 케이스에서 이하의 케이스를 모두 구하는 방식(재귀 - 그치만 일단 캐싱을 함)
        # min을 때려서 : 가능한 최소값을 구해냄

    # 1은 왜 더하는거지
    dp[a][b][c] += 1
    return dp[a][b][c]

scv = [0, 0, 0]

for i in range(len(lst)):
    scv[i] = lst[i]

print(go(scv[0], scv[1], scv[2]))
