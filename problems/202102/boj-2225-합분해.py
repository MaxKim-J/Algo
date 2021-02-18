n, k = map(int, input().split())
dp_prev = [1] * (n+1)
dp = []

for i in range(1, k):
    for j in range(n+1):
        dp.append(sum(dp_prev[:j+1]))
    dp_prev = dp[:]
    dp = []

print(dp_prev[-1] % 1000000000)
