N = int(input())
dp = [1 for i in range(10)]

for _ in range(N-1):
    for i in range(0, 10):
        dp[i] = sum(dp[i:10])

print(sum(dp) % 10007)
