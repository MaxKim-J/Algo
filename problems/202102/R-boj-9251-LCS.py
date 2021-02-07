
# 최장 공통 부분 수열 문제
# 두 수열 길이가 N미만이면 O(n^2)으로
# 문자열의 길이를 늘려가면서 테이블을 갱신
# 테이블의 값은 각 두 문자열의 최장 공통 부분 수열의 길이
# * 점화식 : D[i][j] = D[i-1][j-1] + 1 if x[i] != y[j] OR max(D[i][j-1], D[i-1][j]) if x[i] != y[j]
#! 한 문자열의 자릿수를 하나씩 올려서 탐색하고, 다른 문자열은 전체를 탐색하는데
#! 다른게 나오면 이미 규명한 문자열 최장공통부분수열의 길이 중 큰걸 선택해 업뎃(위와 왼쪽)
#! 같은게 나오면 이미 규명한 문자열 최장공통부분수열 값에다 + 1 (대각선)

x = int(input())
y = int(input())
dp = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]

for i in range(1, len(x) + 1):
    for j in range(1, len(y) + 1):
        if x[i-1] == y[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[len(x)][len(y)])
