# 백준 10844: 쉬운 계단 수
# https://www.acmicpc.net/problem/10844
# 시간 : 60분 초과
# 경과 : 시간초과 -> 틀렸습니다 -> 못품

n = int(input())
dp = [[0 for i in range(10)] for j in range(101)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[n]) % 1000000000)

#! 접근 1 : 동적계획법에서 시간초과가 자꾸 난다면 이차원배열 써야할까 생각해야겠음
#! 접근 2 : 어떤 정보를 계속해서 메모이제이션 해야하나 생각해야함(중요) + 무엇이 편할까
#! 동적 계획법의 뒷 값을 갱신하기위해서는 앞값이 전부+온전히+수정되면 안되는 값이 통쩨로 필요

"""
# 시간초과였던 내 답
# 아마 배열이 계속해서 늘어나니깐 큰 수에서는
# 선형적으로 순회하는 시간이 너무 길었던 것일 테다

import sys

N = int(sys.stdin.readline())
dp = list(range(1, 10))

for _ in range(N-1):
    temp = []
    for num in dp:
        if num < 1:
            temp.append(num+1)
        elif num > 8:
            temp.append(num-1)
        else:
            temp.append(num+1)
            temp.append(num-1)
        dp = temp[:]

print(len(dp) % 1000000000)
"""
