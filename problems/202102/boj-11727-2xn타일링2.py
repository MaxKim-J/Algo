N = int(input())
dp = [0] + [1] + [3] + [0] * 998

if N < 3:
    print(dp[N])
    exit(0)

for i in range(3, N+1):
    dp[i] = dp[i-1] + (dp[i-2] * 2)

print(dp[N] % 10007)
