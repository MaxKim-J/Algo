# 재귀로 풀었던 기억이 있다 => 이번엔 DP로 풀것
#! 점화식이 우선임 => 각 순회에서의 규칙 파악해볼것
#! 최대한 정답 지향적으로 생각할 것 => 보드에 무조건 정답이 적힌다!는 생각

t = int(input())
dp = [1, 2, 4]

for i in range(3, 10):
    dp.append(dp[i - 3] + dp[i - 2] + dp[i - 1])

for i in range(t):
    n = int(input())
    print(dp[n - 1])
