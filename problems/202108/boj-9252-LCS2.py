a = input()
b = input()

# DP테이블 만들때 0부터 시작하게 만들자. 레버리지가 생김
dp = [[0 for i in range(len(a) + 1)] for j in range(len(b) + 1)]

for i in range(1, len(b) + 1):
    for j in range(1, len(a) + 1):
        if a[j - 1] == b[i - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# 역추적 - 대각선 방향부터 추적하여 큰 곳으로 가거나
# 위랑 왼쪽 수가 같으면 대각선으로 간다
# 말 그대로 DP 테이블 채우는 방법을 역으로 사용해서 추적한다
def findit():
    ans = ''
    now = dp[-1][-1]
    y = len(dp) - 1
    x = len(dp[0]) - 1
    while now != 0:
        if dp[y][x - 1] == now - 1 and now - 1 == dp[y - 1][x]:
            ans = a[x - 1] + ans
            now -= 1
            y -= 1
            x -= 1
        else:
            if dp[y - 1][x] > dp[y][x - 1]:
                y -= 1
            else:
                x -= 1
    return ans

print(dp[-1][-1])
print(findit())