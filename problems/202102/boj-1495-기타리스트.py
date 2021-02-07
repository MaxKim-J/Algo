# O(NM) => 왼쪽부터 오른쪽으로 이전값으로 지금값을
# 모든 볼륨에 대하여 연주 가능 여부를 계산해주기
# 노래를 순서대로 확인하고, 매번 모든 크기의 볼륨에 대하여 검사

'''
D[i][j+1] = i번째 노래일때, j크기 볼륨으로 연주 가능한지 여부 검사
최대 볼륨까지 수를 늘이면서?
i = 노래의 번호
V = 볼륨을 다 받은 선형리스트 

DP테이블의 인덱스는 볼륨, row는 곡

이전의 연주가 가능했다면, 거기 기준으로 볼륨을 해당 차이만큼 줄이거나 높일 수 있음
대신 최소최대볼륨 범위 안에 들어가야함
D[i][j - V[i]] = True if D[i-1][j] = True
D[i][j + V[i]] = True if D[i-1][j] = True
'''

n, s, m = map(int, input().split())
volumes = list(map(int, input().split()))

dp = [[0] * (m+1) for _ in range(n+1)]
dp[0][s] = 1

for i in range(1, n+1):
    for j in range(m + 1):
        if dp[i-1][j] == 0:
            continue
        if j-volumes[i-1] >= 0:
            dp[i][j-volumes[i-1]] = 1
        if j+volumes[i-1] <= m:
            dp[i][j+volumes[i-1]] = 1

result = -1
# 최대 볼륨부터 마지막 노래 row의 볼륨중 가장 큰 것(가장 먼저 1인것)을 result에 저장
for i in range(m, -1, -1):
    if dp[n][i] == 1:
        result = i
        break

print(result)
