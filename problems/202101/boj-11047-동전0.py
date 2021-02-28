N, K = map(int, input().split())
coins = sorted([int(input()) for _ in range(N)], reverse=True)
dp = [0]*N

for i in range(N):
    dp[i] = K//coins[i]
    K -= coins[i]*dp[i]

print(sum(dp))
