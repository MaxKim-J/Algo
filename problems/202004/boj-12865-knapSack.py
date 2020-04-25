# 백준 12865: 평범한 배낭
# https://www.acmicpc.net/problem/12865
# 시간 : 60분+
# 경과 : 못품

import sys

r = sys.stdin.readline
N, W = map(int, r().split())
bag = [tuple(map(int, r().split())) for _ in range(N)]

knap = [0 for _ in range(W+1)]

for i in range(N):
    for j in range(W, 1, -1):
        if bag[i][0] <= j:
            knap[j] = max(knap[j], knap[j-bag[i][0]] + bag[i][1])

print(knap[-1])

#! 어려움! 풀이 다시 보면서 이해하긴 했는데 나중에 한번 더 봐야할듯

#! 접근1) 이차원 배열 : 최대무게를 0부터 N까지 가질때, 물품의 인덱스를 어디까지 포함한 배열로 잘라 순회할 것이냐
#! 접근2) 인덱스를 갱신하면서 어떤 값들은 바로 왼쪽에서 가져와야 하고,
#! 어떤 값들은 저번 인덱스의 동일한 최대무게에서 자신의 무게를 뺀 인덱스의 가치에다가 자신의 가치를 더한 값이 됨
#! 구할 최대무게에서 자신의 무게를 빼면, 자신이 들어갈 수 있는 자리가 나온다고 생각해야하나(?) 뭐 그렇다

"""
# 이차원 배열로 풀기

N, W = 4, 5
w = [2, 3, 4, 5]
b = [3, 4, 5, 6]

knap = [[0 for _ in range(W+1)] for _ in range(N+1)]

for i in range(N+1):
    for j in range(W+1):
        if w[i-1] <= j: 
            knap[i][j] = max(b[i-1] + knap[i-1][j-w[i-1]],  knap[i-1][j]) 
        else: 
            knap[i][j] = knap[i-1][j] 

print(knap)
"""
