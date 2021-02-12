# 이천수..?

N = int(input())

if N < 3:
    print(1)
    exit(0)

dp = [1, 0]
for _ in range(2, N):
    dp = [dp[0] + dp[1], dp[0]]

print(sum(dp))
