# 원리만 파악한다면 걍 피보나치 문제였다

N = int(input())
dp = [0] + [1] + [2] + [0] * 998

if N < 3:
    print(dp[N])
    exit(0)

for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N] % 10007)
