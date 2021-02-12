# 이천수..?

N = int(input())
dp = [1, 0]

if N < 3:
    print(1)
    exit(0)

for _ in range(2, N):
    temp = [dp[0] + dp[1], dp[0]]
    dp = temp

print(sum(dp))
