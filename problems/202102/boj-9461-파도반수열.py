t = int(input())
dp = [0, 1, 1, 1, 2]

for i in range(4, 100):
    dp.append(dp[-2] + dp[-3])

for _ in range(t):
    n = int(input())
    print(dp[n])
