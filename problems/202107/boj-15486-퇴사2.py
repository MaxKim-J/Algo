N = int(input())

term = []
price = []

for _ in range(N):
  t, p = map(int, input().split())
  term.append(t)
  price.append(p)

dp = [0] * (N+1)

# 0을 띄워넘는 방식
for i in range(N):
    if term[i] + i <= N:
        dp[i+term[i]] = max(dp[i+term[i]], dp[i]+price[i]) # 마지막이 1일수도 있으니 하나 더 할당
    dp[i+1] = max(dp[i+1], dp[i]) # 하나 더 앞서서 먼저 갱신

print(dp[-1])
