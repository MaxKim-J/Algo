# 백준 11047: 동전 0
# https://www.acmicpc.net/problem/11047
# 시간 : 15분
# 경과 : 맞았습니다(62ms)


N, K = map(int, input().split())
coins = sorted([int(input()) for _ in range(N)], reverse=True)
count = 0

for coin in coins:
    if K == 0:
        break
    new_count = K//coin
    K -= new_count * coin
    count += new_count

print(count)

#! 별건 없었음, 그리디의 아주 기본적인 문제
# * 동전의 조건이 특별해서 dp보다 빠르게 답을 찾을 수 있다고 함(근데 백준 상으로는 64ms로 시간 똑같음)

"""
# dp로 풀었을 때

N, K = map(int, input().split())
coins = sorted([int(input()) for _ in range(N)], reverse=True)
dp = [0]*N

for i in range(N):
    if K == 0:
        break
    dp[i] = K//coins[i]
    K -= coins[i]*dp[i]

print(sum(dp))
"""
